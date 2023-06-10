from api.commands.joke import tell_joke_es


def test_joke_variety():
    assert tell_joke_es([]) is not None
