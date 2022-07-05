"""
NAME
    Translate - This file includes functions for the "translate" GeoSMS command.

FILE
    translate.py

FUNCTIONS
    translate_from_es_to_en: Returns a translation of the arguments as an English sentence.

"""
from typing import List
import translate
from utils import exceptions
import utils


def translate_from_es_to_en(args: List[str]) -> str:
    """
    Returns a translation of the arguments as an English sentence.

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