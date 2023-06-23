// Reference: https://www.mongodb.com/docs/drivers/node/v5.6/usage-examples/insertMany/

const { MongoClient } = require('mongodb');

// Replace the uri string with your MongoDB deployment's connection string.
const uri = "mongodb://localhost:27017";
const client = new MongoClient(uri);

// Collection name and dbname
const dbName = 'DrugsDatabase';
const otc_collectionName = 'fda_otc_drugs';
// const sym_collectionName = 'fda_sym_drugs';

const apiUrl = 'https://api.fda.gov/drug/drugsfda.json?search=products.marketing_status:%22Over-the-counter%22&limit=1000';

async function run() {
  try {
    const database = client.db(dbName);
    try {
      db.createCollection(otc_collectionName);
    }catch(error){
      // collection already exist - do nothing;
    }
    const collection = database.collection(otc_collectionName);
    collection.deleteMany();

    // create an array of documents to insert
    const docs = await fetch(apiUrl).then(response => response.json())
    .then(data => {        
      let lastUpdated = data.meta.last_updated

      return data.results.filter(f=> f.openfda !== undefined).map(d => {
        return {
            "brand_name" : d.openfda.brand_name,
            "generic_name" : d.openfda.generic_name,
            "manufacturer_name" : d.openfda.manufacturer_name,
            "route": d.openfda.route,
            "substance_name": d.openfda.substance_name,
            "products" : d.products
        }
      }); 
    });
    // this option prevents additional documents from being inserted if one fails
    const options = { ordered: true };
    const result = await collection.insertMany(docs, options);
    console.log(`${result.insertedCount} documents were inserted`);
  } finally {
    await client.close();
  }
}run().catch(console.dir);