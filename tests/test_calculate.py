from api.commands.calculate import calculate


def test_calculate_integers():
    assert calculate(["6", "+", "2"]) == "8"
    assert calculate(["6", "-", "2"]) == "4"
    assert calculate(["6", "*", "2"]) == "12"
    assert calculate(["6", "/", "2"]) == "3.0"
    assert calculate(["6", "**", "2"]) == "36"


def test_calculate_decimals():
    assert calculate(["1.5", "+", "2"]) == "3.5"
    assert calculate(["1.5", "-", "2"]) == "-0.5"
    assert calculate(["1.5", "*", "2"]) == "3.0"
    assert calculate(["1.5", "/", "2"]) == "0.75"
    assert calculate(["1.5", "**", "2"]) == "2.25"
