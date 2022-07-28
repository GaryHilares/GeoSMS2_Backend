"""
NAME
    Command processor - This file includes data and methods required for processing GeoSMS commands.

FILE
    command_processor.py

FUNCTIONS
    run_command: Runs the command given as argument.

"""
from api.commands import translate, search, calculate, joke, news
from api.classes import exceptions

metadata = {
    'default_per': {
        'commands': {
            "traducir-es": translate.translate_from_es_to_en,
            "traducir-en": translate.translate_from_en_to_es,
            "noticias": news.scrap_el_comercio,
            "chiste": joke.tell_joke_es,
            "buscar": search.search_in_google_es,
            "calcular": calculate.calculate
        }
    }
}


def run_command(command: str, country: str = 'default_per') -> str:
    """
    Runs the given command

    :param command: The command to run.
    :param country: The country to use while running the command.
    :raises exceptions.UnknownCommandException: If the command isn't known by GeoSMS.
    """
    if not command:
        raise exceptions.UnknownCommandException()
    split_command = command.split()
    base_command = split_command[0].lower()
    if country not in metadata:
        country = 'default'
    if base_command not in metadata[country]['commands']:
        raise exceptions.UnknownCommandException(base_command)
    args = split_command[1:]
    return metadata[country]['commands'][base_command](args)
