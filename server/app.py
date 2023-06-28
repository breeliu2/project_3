# Import the dependencies
import requests, db_config

from flask import Flask, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo

# define query parameters to get data from FDA source data site
# number of records to pull from source
limit_value = db_config.query_limit
# list of types and collection in which the records to be stored
fda_get_col = db_config.db_collections

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# MongoDB Connection
app.config[db_config.mongoURI] = db_config.mongodb_path
mongo = PyMongo(app)

# Flask route to get all Medication's 
@app.route('/getMedicationByType/<medication_type>', methods=['GET'])
def getMedicationByType(medication_type):
    print(medication_type)
    for each_col in fda_get_col:
        if each_col["marketing_status"] == medication_type:
            col = mongo.db.get_collection(each_col['col_name'])
            query =[
                    {'$unwind':"$products"},  
                    {'$unwind':"$products.active_ingredients"},
                    {'$group':{'_id':'null', 'prds': {'$push' : {
                                    'brand_name': "$products.brand_name", 
                                    'active_ingredients': {'$concat': ["$products.active_ingredients.name"," - ","$products.active_ingredients.strength"]},                                    
                                    'dosage_form': "$products.dosage_form",
                                    'route': "$products.route"
                    } } }},
                    { '$sort' : { "prds.brand_name" : 1 } },
                    {'$project':{'_id':0, 'products': "$prds"   }}
                ]   
            res = list(col.aggregate(query))
            return (jsonify(res))


# Flask route to get medication count By results.products.dosage_form or route
@app.route('/getCountByCategory/<medication_type>/<category_type>', methods=['GET'])
def getCountByCategory(medication_type,category_type):
    for each_col in fda_get_col:
        if each_col["marketing_status"] == medication_type:
            col = mongo.db.get_collection(each_col['col_name'])
            query =[
                    {'$unwind':"$products"},  
                    {'$group':{'_id':f"$products.{category_type}", 'count': { '$count': {} }}},
                    { '$sort' : { "_id" : 1 } },
                    {'$project':{'_id':0, f'{category_type}':"$_id", 'count':"$count" } }
                ]   
            res = list(col.aggregate(query))
            return (jsonify(res))


# Flask route to refresh data from data source if requested by the user
@app.route('/refresh_data', methods=['POST'])
def refresh_data():
    res_count = 0
    for each_col in fda_get_col:
        response = requests.get(f'https://api.fda.gov/drug/drugsfda.json?search=products.marketing_status:%22{each_col["marketing_status"]}%22&limit={limit_value}')
        data = response.json()
        filtered_data = filter_records(data)    
        col = mongo.db.get_collection(each_col['col_name'])
        col.delete_many({})
        res = col.insert_many(filtered_data)
        res_count += len(res.inserted_ids)    
    return jsonify(f"Total records refreshed from source:{res_count}")

# Flask route to refresh data from data source if requested by the user
@app.route('/getMoreDetailsFromFDA/<brand_name>', methods=['GET'])
def getMoreDetailsFromFDA(brand_name):
    response = requests.get(f'https://api.fda.gov/drug/label.json?search=openfda.brand_name:"{brand_name}"&limit=1')
    data = response.json()
    if  data.get('results') is not None:
        filtered_data = filter_records(data)    
        return {
            "purpose" : filtered_data[0]["purpose"] if filtered_data[0].get("purpose") is not None else ['Not Available'],
            "warnings" : filtered_data[0]["warnings"] if filtered_data[0].get("warnings") is not None else ['Not Available'],
            "indications_and_usage" : filtered_data[0]["indications_and_usage"] if filtered_data[0].get("indications_and_usage") is not None else ['Not Available']
        }
    else:
        return {
            "Additional_Info": ["Not Available"]
        }                

# Function to conver records in to an array
def filter_records(data):
    filtered_data = []
    for result in data['results']:
        filtered_data.append(result)
    return filtered_data

if __name__ == '__main__':
    app.run(debug=True)
