from api.database import getDatabase
from time import time
import os

COOLDOWN_TIME_SECONDS = 30;

def is_ready(number):
    now = int(time())
    db = getDatabase()
    numbers = db["numbers"]
    number_cooldown = numbers.find_one({"number": number})
    if number_cooldown is None or now >= number_cooldown["expiration"]:
        numbers.update_one({"number": number}, {"$set": {"expiration": now + COOLDOWN_TIME_SECONDS}}, True)
        return True
    else:
        return False
