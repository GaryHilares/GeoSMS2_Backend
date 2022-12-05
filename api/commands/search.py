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
    # Query the API
    query = urllib.parse.quote('+'.join(args), safe='')
    base_url = "https://api.scaleserp.com/search"
    api_key = os.environ.get('SCALESERP_KEY')
    params = {
        'api_key': api_key,
        'q': query,
        'hl': 'es',
    }
    response = requests.get(base_url, params).json()
    answer = ""

    # Log the response
    print(response)

    # Query the API
    if 'knowledge_graph' in response and 'description' in response['knowledge_graph']:
        answer = response["knowledge_graph"]["description"]
    elif 'related_questions' in response and len(response['related_questions']) > 0 and 'answer' in response["related_questions"][0]:
        answer = response["related_questions"][0]["answer"]
    elif 'organic_results' in response and len(response['organic_results']) > 0 and 'snippet' in response["organic_results"][0]:
        answer = response['organic_results'][0]['snippet']
    else:
        answer = "¡Lo siento! No encontramos tu resultado."
    while len(answer) > 150:
        answer = answer[:-1]
        last_point_index = max(
            answer.rindex('.') if '.' in answer else -1,
            answer.rindex('!') if '!' in answer else -1,
            answer.rindex('?') if '?' in answer else -1
        )
        if last_point_index != -1:
            answer = answer[:last_point_index+1]
        else:
            answer = answer[:150]
    return answer
