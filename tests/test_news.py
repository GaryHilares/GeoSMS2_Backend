from api.commands.news import scrap_el_comercio
from dotenv import load_dotenv

load_dotenv()


def test_news_exist():
    assert scrap_el_comercio(["1"]) != "¡Esa noticia no existe!"
