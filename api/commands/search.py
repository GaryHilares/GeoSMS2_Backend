"""
NAME
    Search - This file includes functions for the "search" GeoSMS command.

FILE
    search.py

FUNCTIONS
    search_in_google: Searches the given query in Google and returns an answer to it.

"""
from typing import List
import os
import requests


def search_in_google(args: List[str]) -> str:
    """
    Searches the given query in Google and returns an answer to it.

    :param args: The splitted query.
    :returns: An answer to the given query.
    """
    query = ' '.join(args)
    base_url = "https://api.scaleserp.com/search"
    params = {
        'api_key': os.environ['SERPAPI_KEY'],
        'q': query
    }
    parent = requests.get(base_url, params).json()
    answer = parent["answer_box"]["answers"][0]["answer"]
    return answer
