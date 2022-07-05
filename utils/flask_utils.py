"""
NAME
    flas_utils - This file includes util functions specific to Flask.

FILE
    flask_utils.py

FUNCTIONS
    unescape_markup: Unescapes markup.

"""


def unescape_markup(markup):
    """
    Unescapes markup.

    :param markup: Markup to unescape.
    :returns: Markup with all their escaped characters unescaped.
    """
    return markup.replace('&quot;', '"').replace('&#39;', '\'')
