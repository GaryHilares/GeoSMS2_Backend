from api.commands.search import search_in_google_es


def test_search_important_people():
    president_result = search_in_google_es(["presidente", "perú"]).lower()
    assert "dina" in president_result or "boluarte" in president_result
