from api.commands.translate import translate_from_es_to_en, translate_from_en_to_es


def test_translate_greetings():
    assert translate_from_en_to_es(["hello"]) in ["hola"]
    assert translate_from_es_to_en(["hola"]) in ["hello", "hi"]
    assert translate_from_en_to_es(["good", "morning"]) in [
        "buenos días",
        "buenos dias",
    ]
