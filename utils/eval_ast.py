"""
NAME
    Ast Evaluate - Implementation of arithmetic operations calculation.

FILE
    eval_ast.py

FUNCTIONS
    eval_expr: Evaluates the given mathematical expresion.

"""
# Modified from @jfs's function: https://stackoverflow.com/a/9558001/12170808
import ast
import operator as op

operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}


def eval_expr(expr):
    """
    Evaluates a matemathical expression and returns the result.

    :param expr: The expression to evaluate.
    :return: The result of the given expression.
    """
    return eval_(ast.parse(expr, mode='eval').body)


def eval_(node):
    """
    Helper for the eval_expr function. Evaluates the expression of an ast node recursively.

    :param node: The node to evaluate.
    :return: The result of the given node.
    """
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp):
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)
