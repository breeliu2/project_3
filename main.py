from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# set app.config to point to MogoDB
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/DrugsDatabase"
mongo = PyMongo(app)

# Display index.html
@app.route('/')
def home():
    return render_template('index.html')

# /api/v1.0/druglist shows the available routes
@app.route('/api/v1.0/druglist')
def druglist():
    return (
        f"Available Routes:<br>"
        f'<a href="/api/v1.0/druglist/dbtest">/api/v1.0/druglist/dbtest</a><br>'
        f'<a href="/api/v1.0/druglist/routecount">/api/v1.0/druglist/routecount</a><br>'
        f'<a href="/api/v1.0/druglist/substancecount">/api/v1.0/druglist/substancecount</a><br>'
    )

# Initial test route to test querys and display information
@app.route('/api/v1.0/druglist/dbtest')
def dbtest():

    drugs = mongo.db.fda_otc_drugs.find()
    output = [{'generic_name': drug['generic_name'], 'route':drug['route']} for drug in drugs]

    return jsonify(output)

# route to show information on a paritcular generic drug name
@app.route('/api/v1.0/druglist/generic/<drug_name>')
def generic(drug_name):

    query = {'generic_name': drug_name}
    drugs = mongo.db.fda_otc_drugs.find(query)
    output = [{'generic_name': drug['generic_name'], 'route':drug['route']} for drug in drugs]

    return jsonify(output)

# route to show the possible medication routes and how many drugs use that route
@app.route('/api/v1.0/druglist/routecount')
def routecount():

    query = [{'$group': {'_id': "$route", 'count': { '$sum': 1 }}}]
    routes = list(mongo.db.fda_otc_drugs.aggregate(query))

    output = [{'route': route['_id'], 'count': route['count']} for route in routes]

    return jsonify(output)

# route to show the substance names and how many drugs use that substance
@app.route('/api/v1.0/druglist/substancecount')
def substancecount():

    query = [{'$group': {'_id': "$substance_name", 'count': { '$sum': 1 }}}]
    substances = list(mongo.db.fda_otc_drugs.aggregate(query))

    output = [{'substance_name': substance['_id'], 'count': substance['count']} for substance in substances]

    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)
