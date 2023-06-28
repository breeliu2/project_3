# mongo db database path
mongodb_path = "mongodb://127.0.0.1:27017/DrugsDatabase"
mongoURI = "MONGO_URI"

# number of records to pull from source
query_limit = 100

# list of types and collection in which the records to be stored
db_collections = [
    {
    "marketing_status"   : "Over-the-counter",
    "col_name"           : "fda_otc_drugs"
    },
    {
    "marketing_status"   : "Prescription",
    "col_name"           : "fda_rx_drugs"
    },
    {
    "marketing_status"   : "Discontinued",
    "col_name"           : "fda_dis_drugs"
    }          
]
