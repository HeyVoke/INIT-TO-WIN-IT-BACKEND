# import logging
# import azure.functions as func
# import pymongo
# import os
# from bson.json_util import dumps

# def main(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('💤 get_sleep_data function triggered.')

#     try:
#         # Connect to local MongoDB
#         mongo_uri = "mongodb://localhost:27017"
#         client = pymongo.MongoClient(mongo_uri)
#         db = client["wearable_data"]
#         collection = db["sleep_data"]

#         # Optional: filter by date or user_id
#         query_date = req.params.get("date")
#         query = {"date": query_date} if query_date else {}

#         data = list(collection.find(query))
#         return func.HttpResponse(dumps(data), mimetype="application/json")

#     except Exception as e:
#         logging.error(f"[ERROR] {e}")
#         return func.HttpResponse("Something went wrong.", status_code=500)
import logging
import azure.functions as func
import pymongo
import os
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('💤 get_sleep_data function triggered.')

    try:
        # Use Cosmos DB Mongo URI instead of local Mongo
        mongo_uri = os.getenv("COSMOS_MONGO_URI")  # Store it in local.settings.json or app config
        client = pymongo.MongoClient(mongo_uri)
        db = client["wearable_data"]
        collection = db["sleep_data"]

        query_date = req.params.get("date")
        query = {"date": query_date} if query_date else {}

        data = list(collection.find(query))
        return func.HttpResponse(dumps(data), mimetype="application/json")

    except Exception as e:
        logging.error(f"[ERROR] {e}")
        return func.HttpResponse("Something went wrong.", status_code=500)