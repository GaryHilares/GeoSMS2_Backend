from pymongo import MongoClient
import os

def getDatabase():
    host = os.environ.get('MONGO_HOST')
    user = os.environ.get('MONGO_USER')
    password = os.environ.get('MONGO_PASSWORD')
    client = MongoClient(f"mongodb+srv://{user}:{password}@{host}/?retryWrites=true&w=majority")
    return client.geosms