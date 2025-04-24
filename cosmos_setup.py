from pymongo import MongoClient

# Connection string with placeholder for password
connection_string = "mongodb+srv://t26admin:Chess123@team26mongo2.global.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"

# Connect to the MongoDB client
try:
    client = MongoClient(connection_string)
    print("Connected to CosmosDB successfully!")
    
    # Example: List databases
    databases = client.list_database_names()
    print("Databases:", databases)
except Exception as e:
    print("Failed to connect to CosmosDB:", e)

# make a database
db = client["MindfulCompanion"]

container_names = ["JournalEntries", "MoodScoreTracker", "InitialSignUpSurvey", "SuggestedActions"]
try:
    for container_name in container_names:
            if container_name not in db.list_collection_names():
                db.create_collection(container_name)
                print(f"Container '{container_name}' created successfully!")
            else:
                print(f"Container '{container_name}' already exists.")
except Exception as e:
    print("Failed to create containers:", e)