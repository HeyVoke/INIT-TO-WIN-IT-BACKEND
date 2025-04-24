# ingestion/upload_csv.py

import os
import pandas as pd
from pymongo import MongoClient

# --- Configuration ---
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "wearable_data"
COLLECTION_NAME = "sleep_data"
CSV_FILE = os.path.join(os.path.dirname(__file__), "samples", "example_sleep_data.csv")

def load_csv(csv_path):
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
    print(f"[INFO] Loading CSV from {csv_path}")
    df = pd.read_csv(csv_path)

    # Optional: Clean column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    print(f"[INFO] Loaded {len(df)} rows with columns: {df.columns.tolist()}")
    return df

def upload_to_mongo(df, mongo_uri, db_name, collection_name):
    print(f"[INFO] Connecting to MongoDB at {mongo_uri}")
    client = MongoClient(mongo_uri)
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
        upload_to_mongo(df, MONGO_URI, DB_NAME, COLLECTION_NAME)
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()