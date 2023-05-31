from pymongo import MongoClient
from dotenv import dotenv_values

# Load environment variables from .env file
config = dotenv_values(".env")
mongodb_connection_string = config["MONGODB_CONNECTION_STRING"]
print("mongodb_connection_string" , mongodb_connection_string)

# Connect to MongoDB
def get_database():
    client = MongoClient(mongodb_connection_string)
    db = client["HealthApp"]
    return db


# Connect to MongoDB
def get_database():
    client = MongoClient(mongodb_connection_string)
    db = client["HealthApp"]
    return db

db = get_database()
collection = db["users"]



