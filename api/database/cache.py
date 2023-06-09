from api.database import getDatabase
from time import time

CACHE_DURATION = 10000

def get_cache(query):
    db = getDatabase()
    cache = db["cache"]
    result = cache.find_one({"query": query})
    if not result or int(time()) > result["expiration"]:
       return None
    return result["value"]

def set_cache(query, value):
    db = getDatabase()
    cache = db["cache"]
    cache.update_one({"query": query}, {"$set": {"value": value, "expiration": int(time()) + CACHE_DURATION}}, True)
