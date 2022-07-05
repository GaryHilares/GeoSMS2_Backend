"""
NAME
    Calculate - This file includes functions for the "calculate" GeoSMS command.

FILE
    calculate.py

FUNCTIONS
    calculate: Takes a mathematical expresion and calculates it.

"""
from typing import List
from utils import exceptions
import utils


def calculate(args: List[str]) -> str:
    """
    Takes a mathematical expresion and calculates it.

    :param args: The expression to calculate.
    :returns: The result of the given expression.
    """
    if not args:
        raise exceptions.WrongArguments("calculate", args)
    expression = ' '.join(args)
    return str(utils.eval_ast.eval_expr(expression))
