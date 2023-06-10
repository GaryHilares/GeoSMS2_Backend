"""
NAME
    Search - This file includes functions for the "search" GeoSMS command.

FILE
    search.py

FUNCTIONS
    search_in_google: Searches the given query in Google and returns an answer to it.

"""
import requests
import os
from typing import List
import urllib.parse
import wikipedia


def search_in_wikipedia_es(args: List[str]) -> str:
    """
    Searches the given query in Google and returns an answer to it.

    :param args: The splitted query.
    :returns: An answer to the given query.
    """
    # TODO: Reimplement search feature
    query = " ".join(args)
    wikipedia.set_lang("es")
    page_name = wikipedia.search(query)[0]
    page = wikipedia.summary(page_name, sentences=1)

    # while len(answer) > 150:
    #     answer = answer[:-1]
    #     last_point_index = max(
    #         answer.rindex(".") if "." in answer else -1,
    #         answer.rindex("!") if "!" in answer else -1,
    #         answer.rindex("?") if "?" in answer else -1,
    #     )
    #     if last_point_index != -1:
    #         answer = answer[: last_point_index + 1]
    #     else:
    #         answer = answer[:150]

    return page
