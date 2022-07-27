"""
NAME
    News - This file includes functions for the "news" GeoSMS command.

FILE
    news.py

FUNCTIONS
    scrap_el_comercio: Scraps El Comercio's news and return their headlines.

"""
from typing import List
from requests_html import HTMLSession
from unidecode import unidecode


def scrap_el_comercio(args: List[str]) -> str:
    """
    Scraps [El Comercio](https://elcomercio.pe/)'s news and return their headlines.

    :param args: Words to filter the news headlines.
    :returns: Scrapped and filtered headlines from El Comercio's news.
    """
    session = HTMLSession()
    result = session.get('https://elcomercio.pe/')
    elements = result.html.find('.fs-wi__title')
    news_titles = [element.text for element in elements]
    filtered_news_titles = []
    if args:
        filtered_news_titles = [title for title in news_titles if any(
            unidecode(word).lower() in unidecode(title).lower() for word in args)]
    else:
        filtered_news_titles = news_titles
    if len(filtered_news_titles) > 3:
        filtered_news_titles = filtered_news_titles[:3]
    return '\n'.join(filtered_news_titles)
