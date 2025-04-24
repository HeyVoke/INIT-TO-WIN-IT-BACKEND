from pymongo import MongoClient

COSMOS_URI = "mongodb+srv://t26admin:Chess123@team26mongo2.global.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"
DB_NAME = "MindfulCompanion"

client = MongoClient(COSMOS_URI)
db = client[DB_NAME]

# List all collections (containers)
print("[INFO] Collections in DB:", db.list_collection_names())