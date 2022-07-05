import random
from typing import List


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
