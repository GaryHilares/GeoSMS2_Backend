from pymongo import MongoClient
from time import time
import os

COOLDOWN_TIME_SECONDS = 5;
host = os.environ.get('MONGO_HOST')
user = os.environ.get('MONGO_USER')
password = os.environ.get('MONGO_PASSWORD')
client = MongoClient(f"mongodb+srv://{user}:{password}@{host}/?retryWrites=true&w=majority")
db = client.geosms

def is_ready(number):
    now = int(time())
    numbers = db["numbers"]
    number_cooldown = numbers.find_one({"number": number})
    if number_cooldown is None or now >= number_cooldown["expiration"]:
        numbers.update_one({"number": number}, {"$set": {"expiration": now + COOLDOWN_TIME_SECONDS}}, True)
        return True
    else:
        return False
