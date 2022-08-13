"""
NAME
    Search - This file includes functions for the "search" GeoSMS command.

FILE
    search.py

FUNCTIONS
    search_in_google: Searches the given query in Google and returns an answer to it.

"""
from typing import List
import urllib.parse
import os
import requests


def search_in_google_es(args: List[str]) -> str:
    """
    Searches the given query in Google and returns an answer to it.

    :param args: The splitted query.
    :returns: An answer to the given query.
    """
    query = urllib.parse.quote('+'.join(args), safe='')
    base_url = "https://api.scaleserp.com/search"
    api_key = os.environ.get('SCALESERP_KEY')
    params = {
        'api_key': api_key,
        'q': query,
        'hl': 'es',
    }
    parent = requests.get(base_url, params).json()
    answer = ""
    print(parent)
    if 'knowledge_graph' in parent and 'description' in parent['knowledge_graph']:
        answer = parent["knowledge_graph"]["description"]
    elif 'related_questions' in parent and len(parent['related_questions']) > 0 and 'answer' in parent["related_questions"][0]:
        answer = parent["related_questions"][0]["answer"]
    elif 'organic_results' in parent and len(parent['organic_results']) > 0 and 'snippet' in parent["organic_results"][0]:
        answer = parent['organic_results'][0]['snippet']
    else:
        answer = "¡Lo siento! No encontramos tu resultado."
    while len(answer) > 200:
        answer = answer[:-1]
        last_point_index = max(
            answer.rindex('.') if '.' in answer else -1,
            answer.rindex('!') if '!' in answer else -1,
            answer.rindex('?') if '?' in answer else -1
        )
        if last_point_index != -1:
            answer = answer[:last_point_index+1]
        else:
            answer = answer[:200]
    return answer
