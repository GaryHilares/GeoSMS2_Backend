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
    # Declare the jokes
    jokes = [
        "¿Qué le dice un pato a otro pato? Estamos empatados.",
        "¿Cuál es la bebida favorita de los patos? El quack-er.",
        "¿Qué le dice una foca a otra foca? Enfócate.",
        "¿Qué le dice una piedra a otra piedra? Nada, porque las piedras no hablan.",
    ]
    
    # Choose a random joke from the joke list
    return random.choice(jokes)
