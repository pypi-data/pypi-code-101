# -----------------------------------------------------------------------------
# sheng: parse.py
#
# Copyright (c) 2021
# luojiahai
# All rights reserved.
#
# Latest version: https://github.com/luojiahai/sheng
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# BEGIN parse.py
# -----------------------------------------------------------------------------

from .ply import yacc
from .lex import *
from .ast import *
from .builtins import *
from .exception import *


# Token list
tokens = Lexer().tokens

# Precedence rules
precedence = (
    # ('left', 'OR',),
    # ('left', 'AND',),
    # ('right', 'NOT',),
    ('left', 'EQEQUAL', 'NOTEQUAL', 'LESS', 'GREATER', 'LESSEQUAL', 'GREATEREQUAL',),
    ('left', 'PLUS', 'MINUS',),
    # ('left', 'STAR', 'SLASH', 'DOUBLESLASH', 'PERCENT',),
    # ('right', 'UADD', 'USUB',),
    # ('right', 'DOUBLESTAR',),
)

# Rule for a program
def p_program(p):
    '''program : block
               | empty'''
    block = []
    if (p[1]): block = p[1]
    p[0] = Program(block)

# Rule for block
def p_block(p):
    '''block : statements'''
    p[0] = p[1]

# Rule for statements
def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if (len(p) == 2 and p[1]):
        statement = p[1]
        p[0] = [statement]
    elif (len(p) == 3):
        statements = p[1]
        if (p[2]): statements.append(p[2])
        p[0] = statements

# Rule for statement
def p_statement(p):
    '''statement : statement_assignment
                 | statement_return
                 | statement_pass
                 | statement_assert
                 | statement_break
                 | statement_continue
                 | statement_function_def
                 | statement_if
                 | statement_class_def
                 | statement_iterate
                 | statement_loop
                 | expression'''
    p[0] = p[1]

# Statement rule for assignment
def p_statement_assignment(p):
    '''statement_assignment : NAME EQUAL expression'''
    name = Name(p[1])
    p[0] = Assignment(name, p[3])

# Statement rule for return
def p_statement_return(p):
    '''statement_return : RETURN expression
                        | RETURN'''
    if (len(p) == 2):
        p[0] = Return(None)
    elif (len(p) == 3):
        p[0] = Return(p[2])

# Statement rule for pass
def p_statement_pass(p):
    '''statement_pass : PASS'''
    p[0] = Pass(p[1])

# Statement rule for assert
def p_statement_assert(p):
    '''statement_assert : ASSERT expression'''
    p[0] = Assert(p[2])

# Statement rule for break
def p_statement_break(p):
    '''statement_break : BREAK'''
    p[0] = Break(p[1])

# Statement rule for continue
def p_statement_continue(p):
    '''statement_continue : CONTINUE'''
    p[0] = Continue(p[1])

# Statement rule for function definition
def p_statement_function_def(p):
    '''statement_function_def : FUNCTIONDEF NAME LPAR parameters RPAR BEGIN block END
                              | FUNCTIONDEF NAME LPAR RPAR BEGIN block END'''
    if (len(p) == 8):
        name = Name(p[2])
        body = p[6]
        p[0] = FunctionDef(name, [], body)
    elif (len(p) == 9):
        name = Name(p[2])
        parameters = p[4]
        body = p[7]
        p[0] = FunctionDef(name, parameters, body)

# Statement rule for if
def p_statement_if(p):
    '''statement_if : IF expression THEN block statement_elif END'''
    expression = p[2]
    block = p[4]
    statement_elif = p[5]
    p[0] = If(expression, block, statement_elif=statement_elif)

def p_statement_if_else(p):
    '''statement_if : IF expression THEN block block_else END
                    | IF expression THEN block END'''
    if (len(p) == 6):
        expression = p[2]
        block = p[4]
        p[0] = If(expression, block)
    elif (len(p) == 7):
        expression = p[2]
        block = p[4]
        block_else = p[5]
        p[0] = If(expression, block, block_else=block_else)

# Statement rule for elif
def p_statement_elif(p):
    '''statement_elif : ELIF expression THEN block statement_elif'''
    expression = p[2]
    block = p[4]
    statement_elif = p[5]
    p[0] = [Elif(expression, block)] + statement_elif

def p_statement_elif_else(p):
    '''statement_elif : ELIF expression THEN block block_else
                      | ELIF expression THEN block'''
    if (len(p) == 5):
        expression = p[2]
        block = p[4]
        p[0] = [Elif(expression, block)]
    elif (len(p) == 6):
        expression = p[2]
        block = p[4]
        block_else = p[5]
        p[0] = [Elif(expression, block, block_else=block_else)]

# Rule for else block
def p_block_else(p):
    '''block_else : ELSE block'''
    p[0] = p[2]

# Statement rule for class definition
def p_statement_class_def(p):
    '''statement_class_def : CLASSDEF NAME BEGIN block END'''
    name = Name(p[2])
    block = p[4]
    p[0] = ClassDef(name, block=block)

# Statement rule for iterate
def p_statement_iterate(p):
    '''statement_iterate : ITERATE expression FOR NAME BEGIN block END'''
    iterable = p[2]
    variable = Name(p[4])
    statements = p[6]
    p[0] = Iterate(iterable, variable, statements)

# Statement rule for loop
def p_statement_loop(p):
    '''statement_loop : LOOP expression BEGIN block END'''
    expression = p[2]
    statements = p[4]
    p[0] = Loop(expression, statements)

# Rule for expressions
def p_expressions(p):
    '''expressions : expression comma_expressions COMMA
                   | expression comma_expressions
                   | expression COMMA
                   | expression'''
    if ((len(p) == 3 and p[2] == ',') or len(p) == 2):
        expression = p[1]
        p[0] = [expression]
    elif (len(p) == 4 or len(p) == 3):
        comma_expressions = p[2]
        if (p[1]): comma_expressions.insert(0, p[1])
        p[0] = comma_expressions

# Rule for expressions: (',' expression)+
def p_comma_expressions(p):
    '''comma_expressions : comma_expressions COMMA expression
                         | COMMA expression'''
    if (len(p) == 3):
        expression = p[2]
        p[0] = [expression]
    elif (len(p) == 4):
        comma_expressions = p[1]
        if (p[3]): comma_expressions.append(p[3])
        p[0] = comma_expressions

# Rule for parameters
def p_parameters(p):
    '''parameters : parameter parameters_comma COMMA
                  | parameter parameters_comma
                  | parameter COMMA
                  | parameter'''
    if ((len(p) == 3 and p[2] == ',') or len(p) == 2):
        parameter = p[1]
        p[0] = [parameter]
    elif (len(p) == 4 or len(p) == 3):
        parameters_comma = p[2]
        if (p[1]): parameters_comma.insert(0, p[1])
        p[0] = parameters_comma

# Rule for parameter with no default
def p_parameters_comma(p):
    '''parameters_comma : parameters_comma COMMA parameter
                        | COMMA parameter'''
    if (len(p) == 3):
        paramter = p[2]
        p[0] = [paramter]
    elif (len(p) == 4):
        parameters_comma = p[1]
        if (p[3]): parameters_comma.append(p[3])
        p[0] = parameters_comma

# Rule for parameter
def p_parameter(p):
    '''parameter : NAME'''
    p[0] = Name(p[1])

# Expression rule for group expression
def p_expression_group(p):
    '''expression : LPAR expression RPAR'''
    p[0] = p[2]

# Expression rule for disjunction
def p_expression_disjunction(p):
    '''expression : disjunction'''
    p[0] = p[1]

# Rule for disjunction
def p_disjunction(p):
    '''disjunction : conjunction or_conjunctions
                   | conjunction'''
    if (len(p) == 2):
        p[0] = Disjunction([p[1]])
    elif (len(p) == 3):
        p[0] = Disjunction([p[1]] + p[2])

# Rule for (OR conjunction)+
def p_or_conjunctions(p):
    '''or_conjunctions : or_conjunctions OR conjunction
                       | OR conjunction'''
    if (len(p) == 3):
        p[0] = [p[2]]
    elif (len(p) == 4):
        or_conjunctions = p[1]
        or_conjunctions.append(p[3])
        p[0] = or_conjunctions

# Rule for conjunction
def p_conjunction(p):
    '''conjunction : inversion and_inversions
                   | inversion'''
    if (len(p) == 2):
        p[0] = Conjunction([p[1]])
    elif (len(p) == 3):
        p[0] = Conjunction([p[1]] + p[2])

# Rule for (AND inversion)+
def p_and_inversions(p):
    '''and_inversions : and_inversions AND inversion
                      | AND inversion'''
    if (len(p) == 3):
        p[0] = [p[2]]
    elif (len(p) == 4):
        and_inversions = p[1]
        and_inversions.append(p[3])
        p[0] = and_inversions

# Rule for inversion
def p_inversion(p):
    '''inversion : NOT inversion
                 | comparison'''
    if (len(p) == 2):
        p[0] = p[1]
    elif (len(p) == 3):
        p[0] = Inversion(p[2])

# Rule for comparison
def p_comparison(p):
    '''comparison : sum EQEQUAL sum
                  | sum NOTEQUAL sum
                  | sum LESS sum
                  | sum LESSEQUAL sum
                  | sum GREATER sum
                  | sum GREATEREQUAL sum
                  | sum'''
    if (len(p) == 2):
        p[0] = p[1]
    else:
        left = p[1]
        right = p[3]
        operator = EXACT_TOKEN_TYPES[p[2]]
        if (operator == 'EQEQUAL'):
            p[0] = Equal(left, right)
        elif (operator == 'NOTEQUAL'):
            p[0] = NotEqual(left, right)
        elif (operator == 'LESS'):
            p[0] = Less(left, right)
        elif (operator == 'LESSEQUAL'):
            p[0] = LessEqual(left, right)
        elif (operator == 'GREATER'):
            p[0] = Greater(left, right)
        elif (operator == 'GREATEREQUAL'):
            p[0] = GreaterEqual(left, right)

# Rule for sum
def p_sum(p):
    '''sum : sum PLUS term
           | sum MINUS term
           | term'''
    if (len(p) == 2):
        p[0] = p[1]
    else:
        left = p[1]
        right = p[3]
        operator = EXACT_TOKEN_TYPES[p[2]]
        if (operator == 'PLUS'):
            p[0] = Add(left, right)
        elif (operator == 'MINUS'):
            p[0] = Subtract(left, right)

# Rule for term
def p_term(p):
    '''term : term STAR factor
            | term SLASH factor
            | term DOUBLESLASH factor
            | term PERCENT factor
            | factor'''
    if (len(p) == 2):
        p[0] = p[1]
    else:
        left = p[1]
        right = p[3]
        operator = EXACT_TOKEN_TYPES[p[2]]
        if (operator == 'STAR'):
            p[0] = Multiply(left, right)
        elif (operator == 'SLASH'):
            p[0] = Divide(left, right)
        elif (operator == 'DOUBLESLASH'):
            p[0] = FloorDivide(left, right)
        elif (operator == 'PERCENT'):
            p[0] = Modulo(left, right)

# Rule for factor
def p_factor(p):
    '''factor : PLUS factor
              | MINUS factor
              | power'''
    if (len(p) == 2):
        p[0] = p[1]
    else:
        value = p[2]
        operator = EXACT_TOKEN_TYPES[p[1]]
        if (operator == 'PLUS'):
            p[0] = UAdd(value)
        elif (operator == 'MINUS'):
            p[0] = USubtract(value)

# Rule for power
def p_power(p):
    '''power : atom DOUBLESTAR factor
             | atom'''
    if (len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = Power(p[1], p[3])

# Atom rule for name
def p_atom_name(p):
    '''atom : NAME'''
    p[0] = Name(p[1])

# Atom rule for boolean
def p_atom_boolean(p):
    '''atom : TRUE
            | FALSE'''
    atom = EXACT_TOKEN_TYPES[p[1]]
    if (atom == 'TRUE'):
        p[0] = Boolean(1)
    elif (atom == 'FALSE'):
        p[0] = Boolean(0)

# Atom rule for null
def p_atom_null(p):
    '''atom : NULL'''
    p[0] = Null(None)

# Atom rule for string
def p_atom_string(p):
    '''atom : STRING'''
    p[0] = String(p[1])

# Atom rule for integer number
def p_atom_integer(p):
    '''atom : INTEGER'''
    p[0] = Integer(p[1])

# Atom rule for float number
def p_atom_float(p):
    '''atom : FLOAT'''
    p[0] = Float(p[1])

# Atom rule for complex number
def p_atom_complex(p):
    '''atom : COMPLEX'''
    p[0] = Complex(p[1])

# Atom rule for tuple
def p_atom_tuple(p):
    '''atom : LPAR expressions RPAR
            | LPAR RPAR'''
    if (len(p) == 3):
        p[0] = Tuple([])
    elif (len(p) == 4):
        expressions = p[2]
        p[0] = Tuple(expressions)

# Atom rule for list
def p_atom_list(p):
    '''atom : LSQB expressions RSQB
            | LSQB RSQB'''
    if (len(p) == 3):
        p[0] = List([])
    elif (len(p) == 4):
        expressions = p[2]
        p[0] = List(expressions)

# Atom rule for dict
def p_atom_dict(p):
    '''atom : LBRACE key_value_pairs RBRACE
            | LBRACE RBRACE'''
    if (len(p) == 3):
        p[0] = Dict([])
    elif (len(p) == 4):
        key_value_pairs = p[2]
        p[0] = Dict(key_value_pairs)

# Rule for key-value pairs
def p_key_value_pairs(p):
    '''key_value_pairs : key_value_pairs COMMA key_value_pair
                       | key_value_pair'''
    if (len(p) == 2 and p[1]):
        key_value_pair = p[1]
        p[0] = [key_value_pair]
    elif (len(p) == 4):
        key_value_pairs = p[1]
        if (p[3]): key_value_pairs.append(p[3])
        p[0] = key_value_pairs

# Rule for key-value pair
def p_key_value_pair(p):
    '''key_value_pair : expression COLON expression'''
    expression_key = p[1]
    expression_value = p[3]
    p[0] = KeyValuePair(expression_key, expression_value)

# Atom rule for iterable index
def p_atom_iterable_index(p):
    '''atom : NAME INDEX expression'''
    name = Name(p[1])
    expression = p[3]
    p[0] = IterableIndex(name, expression)

# Atom rule for function call
def p_atom_functioncall(p):
    '''atom : function_call'''
    p[0] = p[1]

# Rule for function call
def p_functioncall(p):
    '''function_call : NAME LPAR expressions RPAR
                     | NAME LPAR RPAR'''
    if (len(p) == 4):
        name = Name(p[1])
        p[0] = FunctionCall(name, [])
    elif (len(p) == 5):
        name = Name(p[1])
        expressions = p[3]
        p[0] = FunctionCall(name, expressions)

# Atom rule for class member call
def p_atom_classmembercall(p):
    '''atom : class_member_call'''
    name = p[1][0]
    methods = p[1][1:]
    p[0] = ClassMemberCall(name, methods)

# Rule for class member call
def p_classmembercall(p):
    '''class_member_call : class_member_call DOT function_call
                         | class_member_call DOT NAME
                         | NAME DOT function_call'''
    if (len(p) == 4 and type(p[1]) == str):
        p[0] = [Name(p[1]), p[3]]
    elif (len(p) == 4):
        class_member_call = p[1]
        if (p[3]):
            if (type(p[3]) == str): 
                class_member_call.append(Name(p[3]))
            else:
                class_member_call.append(p[3])
        p[0] = class_member_call

# Rule for nothing
def p_empty(p):
    '''empty : '''
    pass

# Error rule for syntax error
def p_error(p):
    if (p):
        raise SyntaxException(f'无效的标记 \'{p.value}\'，第 {p.lineno} 行')
    else:
        raise SyntaxException(f'文件结尾')


# -----------------------------------------------------------------------------
# END parse.py
# -----------------------------------------------------------------------------
