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
from api.database.cache import get_cache, set_cache


def scrap_el_comercio(args: List[str]) -> str:
    """
    Scraps [El Comercio](https://elcomercio.pe/)'s news and return their headlines.

    :param args: Words to filter the news headlines.
    :returns: Scrapped and filtered headlines from El Comercio's news.
    """
    title = get_cache(f"elco-{'-'.join(args)}")
    if not title:
        # Parse args
        filters, index_1indexed = (args[1:], int(args[0])) if args and args[0].isnumeric() else (args, 0)

        # Scrap news titles from El Comercio
        session = HTMLSession()
        result = session.get('https://elcomercio.pe/')
        elements = result.html.find('.fs-wi__title')
        news_titles = [element.text for element in elements]

        # Filter news titles according to parameters
        filtered_news_titles = []
        if filters:
            filtered_news_titles = [title for title in news_titles if any(
                unidecode(word).lower() in unidecode(title).lower() for word in filters)]
        else:
            filtered_news_titles = news_titles

        # Cut first
        if not (index_1indexed >= 1 and index_1indexed <= len(filtered_news_titles)):
            return "¡Esa noticia no existe!"
        
        # Remove leading spaces
        title = filtered_news_titles[index_1indexed - 1].strip()

        set_cache(f"elco-{'-'.join(args)}", title)
    
    return title
