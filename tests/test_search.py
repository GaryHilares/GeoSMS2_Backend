from api.commands.search import search_in_wikipedia_es


def test_search_important_people():
    assert all(
        term in search_in_wikipedia_es(["dina", "boluarte"]).lower()
        for term in ["dina", "boluarte", "abogada"]
    )
