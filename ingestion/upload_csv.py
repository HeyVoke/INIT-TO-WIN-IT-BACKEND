# # # ingestion/upload_csv.py

# # import os
# # import pandas as pd
# # from pymongo import MongoClient

# # # --- Configuration ---
# # MONGO_URI = "mongodb://localhost:27017"
# # DB_NAME = "wearable_data"
# # COLLECTION_NAME = "sleep_data"
# # CSV_FILE = os.path.join(os.path.dirname(__file__), "samples", "example_sleep_data_new.csv")

# # def load_csv(csv_path):
# #     if not os.path.exists(csv_path):
# #         raise FileNotFoundError(f"CSV file not found: {csv_path}")
# #     print(f"[INFO] Loading CSV from {csv_path}")
# #     df = pd.read_csv(csv_path)

# #     # Optional: Clean column names
# #     df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# #     print(f"[INFO] Loaded {len(df)} rows with columns: {df.columns.tolist()}")
# #     return df

# # def upload_to_mongo(df, mongo_uri, db_name, collection_name):
# #     print(f"[INFO] Connecting to MongoDB at {mongo_uri}")
# #     client = MongoClient(mongo_uri)
# #     db = client[db_name]
# #     collection = db[collection_name]

# #     # Optional: Clear old data
# #     # collection.delete_many({})

# #     records = df.to_dict(orient="records")
# #     result = collection.insert_many(records)
# #     print(f"[SUCCESS] Inserted {len(result.inserted_ids)} documents into {db_name}.{collection_name}")

# # def main():
# #     try:
# #         df = load_csv(CSV_FILE)
# #         upload_to_mongo(df, MONGO_URI, DB_NAME, COLLECTION_NAME)
# #     except Exception as e:
# #         print(f"[ERROR] {e}")

# # if __name__ == "__main__":
# #     main()

# import os
# import pandas as pd
# from azure.cosmos import CosmosClient, PartitionKey

# # --- Configuration ---
# COSMOS_URI = "<your-cosmos-db-uri>"  # Replace with your Cosmos DB URI
# COSMOS_KEY = "<your-cosmos-db-key>"  # Replace with your Cosmos DB key
# DB_NAME = "wearable_data"
# CONTAINER_NAME = "sleep_data"
# CSV_FILE = os.path.join(os.path.dirname(__file__), "samples", "example_sleep_data_new.csv")

# def load_csv(csv_path):
#     if not os.path.exists(csv_path):
#         raise FileNotFoundError(f"CSV file not found: {csv_path}")
#     print(f"[INFO] Loading CSV from {csv_path}")
#     df = pd.read_csv(csv_path)

#     # Optional: Clean column names
#     df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

#     print(f"[INFO] Loaded {len(df)} rows with columns: {df.columns.tolist()}")
#     return df

# def upload_to_cosmos(df, cosmos_uri, cosmos_key, db_name, container_name):
#     print(f"[INFO] Connecting to Cosmos DB at {cosmos_uri}")

#     # Create Cosmos Client
#     client = CosmosClient(cosmos_uri, cosmos_key)

#     # Create database if it doesn't exist
#     try:
#         database = client.get_database_client(db_name)
#     except Exception:
#         database = client.create_database(db_name)

#     # Create container if it doesn't exist
#     try:
#         container = database.get_container_client(container_name)
#     except Exception:
#         container = database.create_container(
#             id=container_name,
#             partition_key=PartitionKey(path="/date"),  # Assuming 'date' is a field to partition by
#             offer_throughput=400
#         )

#     # Convert DataFrame to list of dictionaries for Cosmos DB
#     records = df.to_dict(orient="records")

#     # Upload data to Cosmos DB
#     for record in records:
#         container.upsert_item(record)  # upsert (insert or update) each record
#     print(f"[SUCCESS] Uploaded {len(records)} documents to {db_name}.{container_name}")

# def main():
#     try:
#         df = load_csv(CSV_FILE)
#         upload_to_cosmos(df, COSMOS_URI, COSMOS_KEY, DB_NAME, CONTAINER_NAME)
#     except Exception as e:
#         print(f"[ERROR] {e}")

# if __name__ == "__main__":
#     main()
import os
import pandas as pd
from pymongo import MongoClient

# --- Configuration ---
COSMOS_URI = "mongodb+srv://t26admin:Chess123@team26mongo2.global.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"
DB_NAME = "MindfulCompanion"
COLLECTION_NAME = "SleepData"
CSV_FILE = os.path.join(os.path.dirname(__file__), "samples", "example_sleep_data_new.csv")

def load_csv(csv_path):
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
    print(f"[INFO] Loading CSV from {csv_path}")
    df = pd.read_csv(csv_path)

    # Optional: Clean column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    print(f"[INFO] Loaded {len(df)} rows with columns: {df.columns.tolist()}")
    return df

def upload_to_cosmos_mongo(df, cosmos_uri, db_name, collection_name):
    print(f"[INFO] Connecting to Cosmos DB MongoDB API at {cosmos_uri}")
    client = MongoClient(cosmos_uri)
    db = client[db_name]
    collection = db[collection_name]

    # Optional: Clear old data
    # collection.delete_many({})

    records = df.to_dict(orient="records")
    result = collection.insert_many(records)
    print(f"[SUCCESS] Inserted {len(result.inserted_ids)} documents into {db_name}.{collection_name}")


def main():
    try:
        df = load_csv(CSV_FILE)
        upload_to_cosmos_mongo(df, COSMOS_URI, DB_NAME, COLLECTION_NAME)
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()