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
from api.control import exceptions


def unescape_markup(markup):
    """
    Unescapes markup.

    :param markup: Markup to unescape.
    :returns: Markup with all their escaped characters unescaped.
    """
    return markup.replace("&quot;", '"').replace("&#39;", "'")


def translate_from_es_to_en(args: List[str]) -> str:
    """
    Returns a translation of the arguments as an English sentence.

    :param args: The splitted sentence to translate.
    :returns: Translation of the sentence to English.
    :raises exceptions.WrongArguments: If `args` is an empty list.
    """
    # Get text to translate
    if not args:
        raise exceptions.WrongArguments("translate_from_es_to_en", args)
    text = " ".join(args)

    # Translate text
    translator = translate.Translator(from_lang="es", to_lang="en")
    escaped_translated_text = translator.translate(text)

    # Unescape special characters like '.
    translated_text = unescape_markup(escaped_translated_text)

    # Check text length
    return (
        translated_text
        if len(translated_text) < 150
        else "¡Tu texto es muy largo! Intenta acórtarlo."
    )


def translate_from_en_to_es(args: List[str]) -> str:
    """
    Returns a translation of the arguments as an Spanish sentence.

    :param args: The splitted sentence to translate.
    :returns: Translation of the sentence to English.
    :raises exceptions.WrongArguments: If `args` is an empty list.
    """
    # Get text to translate
    if not args:
        raise exceptions.WrongArguments("translate_from_en_to_es", args)
    text = " ".join(args)

    # Translate text
    translator = translate.Translator(from_lang="en", to_lang="es")
    escaped_translated_text = translator.translate(text)

    # Unescape special characters like '.
    translated_text = unescape_markup(escaped_translated_text)

    # Check text length
    return (
        translated_text
        if len(translated_text) < 150
        else "¡Tu texto es muy largo! Intenta acórtarlo."
    )
