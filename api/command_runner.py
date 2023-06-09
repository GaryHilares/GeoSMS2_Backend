"""
NAME
    Command processor - This file includes data and methods required for processing GeoSMS commands.

FILE
    command_processor.py

FUNCTIONS
    run_command: Runs the command given as argument.

"""
from api.commands import translate, search, calculate, joke, news, currency
from api.control import exceptions

commands = {
    "traducir-esp": translate.translate_from_es_to_en,
    "traducir-ing": translate.translate_from_en_to_es,
    "noticia": news.scrap_el_comercio,
    "chiste": joke.tell_joke_es,
    "buscar": search.search_in_google_es,
    "calcular": calculate.calculate,
    "moneda": currency.get_exchange_rate
}

def run_command(command: str) -> str:
    """
    Runs the given command

    :param command: The command to run.
    :raises exceptions.UnknownCommandException: If the command isn't known by GeoSMS.
    """
    if not command:
        raise exceptions.UnknownCommandException()
    split_command = command.split()
    base_command = split_command[0].lower()
    args = split_command[1:]
    if base_command not in commands:
        raise exceptions.UnknownCommandException(base_command)
    return commands[base_command](args)
