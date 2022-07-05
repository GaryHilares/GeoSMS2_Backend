"""
NAME
    Commands - This file includes functions which represent the GeoSMS commands.

FILE
    commands.py

FUNCTIONS
    translate_from_es_to_en: Translates the argument from Spanish to English.
    scrap_el_comercio: Scraps [El Comercio](https://elcomercio.pe/) and return its headlines.
    tell_joke_es: Returns a joke in Spanish.
    search_in_google: Searches the given query in Google and returns an answer to it.
    calculate: Takes a mathematical expresion and calculates it.

"""
import os
import random
from typing import List
import requests
from requests_html import HTMLSession
import translate
from unidecode import unidecode
from utils import exceptions
import utils


def translate_from_es_to_en(args: List[str]) -> str:
    """
    Transforms the arguments into a sentence in Spanish and returns a translation of it to English.

    :param args: The splitted sentence to translate.
    :returns: Translation of the sentence to English.
    :raises exceptions.WrongArguments: If `args` is an empty list.
    """
    if not args:
        raise exceptions.WrongArguments("translate_from_es_to_en", args)
    text = ' '.join(args)
    translator = translate.Translator(from_lang="es", to_lang="en")
    translated_text = translator.translate(text)
    # Unescape special characters like '.
    return utils.flask_utils.unescape_markup(translated_text)


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
    return '\n'.join(filtered_news_titles)


def tell_joke_es(
    args: List[str]  # pylint: disable=unused-argument
) -> str:
    """
    Returns a joke in Spanish.

    :param args: Unused, kept for compability with the command interface.
    :returns: A random joke in Spanish.
    """
    jokes = [
        "¿Qué le dice un pato a otro pato? Estamos empatados.",
        "¿Qué le dice una foca a otra foca? Enfócate.",
        "¿Qué le dice una piedra a otra piedra? Nada, porque las piedras no hablan."
    ]
    return random.choice(jokes)


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


def calculate(args: List[str]) -> str:
    """
    Takes a mathematical expresion and calculates it.

    :param args: The expression to calculate.
    :returns: The result of the given expression.
    """
    if not args:
        raise exceptions.WrongArguments("calculate", args)
    expression = ' '.join(args)
    return str(utils.eval_ast.eval_expr(expression))
