import numpy as np
from sympy import lambdify
from .utils import compare_functions
from sympy.core.sympify import SympifyError

def formula_to_function(formula, variables):

    func = lambdify(variables, formula)
    return func


def assert_answer_is_right(expected, submitted):

    output = {
        'isRight': True,
        'tests': []
    }

    for expected_key, submitted_expression in zip(expected, submitted):

        test = assert_formula_are_equal(expected[expected_key], submitted_expression)
        if not test['isRight']:
            output['isRight'] = False

        output['tests'].append(test)

    return output

def assert_formula_are_equal(expected, submitted):
    
    from sympy.parsing.sympy_parser import parse_expr
    try:
      
        sympy_expected = parse_expr(expected)
        sympy_submited = parse_expr(submitted)
        
    except SympifyError as e:

        return {
            'isRight': 0,
            'stderr': "error.syntax: " + e,
        }
    except SyntaxError as e:
        return {
            'isRight': 0,
            'stderr': "error.syntax"
        }

    return {
        'isRight': sympy_submited.equals(sympy_expected),
        'message': ''
    }

    return output


def plot_formula(formula, variables, ranges):

    pass



