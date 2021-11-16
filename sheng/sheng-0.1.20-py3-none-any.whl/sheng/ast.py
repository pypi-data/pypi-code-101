# -----------------------------------------------------------------------------
# sheng: ast.py
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
# BEGIN ast.py
# -----------------------------------------------------------------------------

from abc import *
from .context import *
from .exception import *
from .builtins import *


# -----------------------------------------------------------------------------
# Generic node class for Abstract Syntax Tree
# -----------------------------------------------------------------------------

class ASTNode(ABC):

    def evaluate(self, context):
        raise NotImplementedError()


# -----------------------------------------------------------------------------
# Utility class for Abstract Syntax Tree
# -----------------------------------------------------------------------------

class ASTUtil(object):

    def evaluate_base_type(value):
        type_name = type(value).__name__
        base_types = [e.__name__ for e in BUILTIN_TYPES.values()]
        if (type_name in base_types):
            return value
        elif (type_name in BUILTIN_TYPES):
            base_type = BUILTIN_TYPES[type_name]
            return base_type(value)
        else:
            raise RuntimeException(f'无效的操作数类型 {type_name}')

    def evaluate_block(context, sequence):
        for node in sequence:
            value = node.evaluate(context)
            if (value):
                return value
        return None

    def instantiate_class(context, classdef):
        instance = ClassType(classdef.name.identifier)
        properties = classdef.properties
        methods = classdef.methods

        # Insert parent symbols to class context
        for _, s in context.symtable.symbols.items():
            instance.context.symtable.insert(s.identifier, s.node)

        # Evaluate assignment statements
        for _, statement in properties.items():
            statement.evaluate(instance.context)

        # Evaluate function def statements
        for _, statement in methods.items():
            statement.evaluate(instance.context)
        
        # Check if a constructor defined, evaluate if so
        if ('构造' in methods):
            functiondef = methods['构造']
            functioncall = FunctionCall(Name('构造'), functiondef.parameters)
            functioncall.evaluate(instance.context)
            
        return instance


# -----------------------------------------------------------------------------
# Program
# -----------------------------------------------------------------------------

class Program(ASTNode):

    def __init__(self, block):
        self._block = block

    @property
    def block(self):
        return self._block

    def evaluate(self, context):
        return ASTUtil.evaluate_block(
            context, self.block
        )


# -----------------------------------------------------------------------------
# Statement
# -----------------------------------------------------------------------------

class Statement(ASTNode): pass


# -----------------------------------------------------------------------------
# Assignment statement
# -----------------------------------------------------------------------------

class Assignment(Statement):

    def __init__(self, name, node):
        self._name = name
        self._node = node

    @property
    def name(self):
        return self._name

    @property
    def node(self):
        return self._node

    def evaluate(self, context):
        identifier = self.name.identifier
        node = Atom(self.node.evaluate(context))
        context.symtable.insert(identifier, node)
        return None


# -----------------------------------------------------------------------------
# Pass statement
# -----------------------------------------------------------------------------

class Pass(Statement):

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def evaluate(self, context):
        pass


# -----------------------------------------------------------------------------
# Assert statement
# -----------------------------------------------------------------------------

class Assert(Statement):

    def __init__(self, expression):
        self._expression = expression

    @property
    def expression(self):
        return self._expression

    def evaluate(self, context):
        if (not self.expression.evaluate(context)):
            raise AssertionException()
        return None


# -----------------------------------------------------------------------------
# Return statement
# -----------------------------------------------------------------------------

class Return(Statement):

    def __init__(self, expression):
        self._expression = expression

    @property
    def expression(self):
        return self._expression

    def evaluate(self, context):
        value = self.expression.evaluate(context)
        ReturnValue = type('ReturnValue', (type(value), ), {})
        return ReturnValue(value)


# -----------------------------------------------------------------------------
# Break statement
# -----------------------------------------------------------------------------

class Break(Statement):

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def evaluate(self, context):
        BreakValue = type('BreakValue', (object, ), {})
        return BreakValue()


# -----------------------------------------------------------------------------
# Continue statement
# -----------------------------------------------------------------------------

class Continue(Statement):

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def evaluate(self, context):
        ContinueValue = type('ContinueValue', (object, ), {})
        return ContinueValue()


# -----------------------------------------------------------------------------
# Function definition statement
# -----------------------------------------------------------------------------

class FunctionDef(Statement, BaseType):

    def __init__(self, name, parameters, body, default_args=[]):
        BaseType.__init__(self, '函数')
        self._name = name
        self._parameters = parameters
        self._body = body
        self._default_args = default_args

    @property
    def name(self):
        return self._name

    @property
    def parameters(self):
        return self._parameters

    @property
    def body(self):
        return self._body

    @property
    def default_args(self):
        return self._default_args

    def evaluate(self, context):
        identifier = self.name.identifier
        context.symtable.insert(identifier, self)
        return None


# -----------------------------------------------------------------------------
# If and Elif statements
# -----------------------------------------------------------------------------

class If(Statement):

    def __init__(self, expression, statements, 
                 statement_elif=[], block_else=None):
        self._expression = expression
        self._statements = statements
        self._statement_elif = statement_elif
        self._block_else = block_else

    @property
    def expression(self):
        return self._expression
    
    @property
    def statements(self):
        return self._statements

    @property
    def statement_elif(self):
        return self._statement_elif

    @property
    def block_else(self):
        return self._block_else

    def evaluate(self, context):
        if (self.expression.evaluate(context)):
            return ASTUtil.evaluate_block(
                context, self.statements
            )
        else:
            # If there exists an elif statement
            for statement_elif in self.statement_elif:
                if (statement_elif.is_true(context)):
                    return statement_elif.evaluate(context)
                elif (statement_elif.block_else):
                    return ASTUtil.evaluate_block(
                        context, statement_elif.block_else
                    )
            
            # If there exists an else block
            if (self.block_else):
                return ASTUtil.evaluate_block(
                    context, self.block_else
                )
            return None


class Elif(Statement):

    def __init__(self, expression, statements, block_else=None):
        self._expression = expression
        self._statements = statements
        self._block_else = block_else

    @property
    def expression(self):
        return self._expression
    
    @property
    def statements(self):
        return self._statements

    @property
    def block_else(self):
        return self._block_else

    def is_true(self, context):
        return self.expression.evaluate(context)

    def evaluate(self, context):
        for node in self.statements:
            value = node.evaluate(context)
            if (value):
                return value
        return None


# -----------------------------------------------------------------------------
# Class definition statement
# -----------------------------------------------------------------------------

class ClassDef(Statement, BaseType):

    def __init__(self, name, block=[]):
        BaseType.__init__(self, '类')
        self._name = name
        properties = dict()
        methods = dict()
        for statement in block:
            if (type(statement) == Assignment):
                properties[statement.name.identifier] = statement
            elif (type(statement) == FunctionDef):
                methods[statement.name.identifier] = statement
        self._properties = properties
        self._methods = methods
    
    @property
    def name(self):
        return self._name

    @property
    def properties(self):
        return self._properties

    @property
    def methods(self):
        return self._methods

    def evaluate(self, context):
        identifier = self.name.identifier
        context.symtable.insert(identifier, self)
        return None


# -----------------------------------------------------------------------------
# Iterate statement
# -----------------------------------------------------------------------------

class Iterate(Statement):

    def __init__(self, iterable, variable, statements):
        self._iterable = iterable
        self._variable = variable
        self._statements = statements

    @property
    def iterable(self):
        return self._iterable
    
    @property
    def variable(self):
        return self._variable

    @property
    def statements(self):
        return self._statements

    def evaluate(self, context):
        variable_identifier = self.variable.identifier
        for e in self.iterable.evaluate(context):
            node = Atom(e)
            context.symtable.insert(variable_identifier, node)
            value = ASTUtil.evaluate_block(
                context, self.statements
            )
            if (type(value).__name__ == 'ReturnValue'):
                return value
            if (type(value).__name__ == 'ContinueValue'):
                continue
            if (type(value).__name__ == 'BreakValue'):
                break
        return None


# -----------------------------------------------------------------------------
# Loop statement
# -----------------------------------------------------------------------------

class Loop(Statement):

    def __init__(self, expression, statements):
        self._expression = expression
        self._statements = statements

    @property
    def expression(self):
        return self._expression
    
    @property
    def statements(self):
        return self._statements

    def evaluate(self, context):
        while (self.expression.evaluate(context)):
            value = ASTUtil.evaluate_block(
                context, self.statements
            )
            if (type(value).__name__ == 'ReturnValue'):
                return value
            if (type(value).__name__ == 'ContinueValue'):
                continue
            if (type(value).__name__ == 'BreakValue'):
                break
        return None


# -----------------------------------------------------------------------------
# Expression
# -----------------------------------------------------------------------------

class Expression(ASTNode): pass


# -----------------------------------------------------------------------------
# Boolean operator expressions
# -----------------------------------------------------------------------------

class Disjunction(Expression):

    def __init__(self, conjunctions):
        self._conjunctions = conjunctions
    
    @property
    def conjunctions(self):
        return self._conjunctions

    def evaluate(self, context):
        if (len(self.conjunctions) == 1):
            return self.conjunctions[0].evaluate(context)
        else:
            value = self.conjunctions[0].evaluate(context)
            for conjunction in self.conjunctions[1:]:
                if (type(conjunction) != Inversion):
                    value = value or conjunction.evaluate(context)
            return ASTUtil.evaluate_base_type(value)


class Conjunction(Expression):

    def __init__(self, inversions):
        self._inversions = inversions
    
    @property
    def inversions(self):
        return self._inversions

    def evaluate(self, context):
        if (len(self.inversions) == 1):
            return self.inversions[0].evaluate(context)
        else:
            value = self.inversions[0].evaluate(context)
            for inversion in self.inversions[1:]:
                if (type(inversion) != Inversion):
                    value = value and inversion.evaluate(context)
            return ASTUtil.evaluate_base_type(value)


class Inversion(Expression):

    def __init__(self, inversion):
        self._inversion = inversion

    @property
    def inversion(self):
        return self._inversion

    def traverse(self, inversion, context):
        if (type(inversion) != Inversion):
            return not inversion.evaluate(context)
        else:
            return not self.traverse(inversion.inversion, context)
    
    def evaluate(self, context):
        return ASTUtil.evaluate_base_type(
            self.traverse(self.inversion, context)
        )


class Comparison(Expression):

    def __init__(self, comparison):
        self._comparison = comparison
    
    @property
    def comparison(self):
        return self._comparison

    def traverse(self, comparison, context):
        if (not isinstance(comparison.left, CompareOp)):
            return comparison.evaluate(context)
        else:
            left = Boolean(self.traverse(comparison.left, context))
            right = comparison.right
            compare = comparison.__class__(left, right)
            return compare.evaluate(context)
    
    def evaluate(self, context):
        return ASTUtil.evaluate_base_type(
            self.traverse(self.comparison, context)
        )


# -----------------------------------------------------------------------------
# Unary operator expressions
# -----------------------------------------------------------------------------

class UnaryOp(Expression):

    def __init__(self, node):
        self._node = node

    @property
    def node(self):
        return self._node


class UAdd(UnaryOp):

    def evaluate(self, context):
        value = self.node.evaluate(context)
        return ASTUtil.evaluate_base_type(+value)


class USubtract(UnaryOp):

    def evaluate(self, context):
        value = self.node.evaluate(context)
        return ASTUtil.evaluate_base_type(-value)


# -----------------------------------------------------------------------------
# Binary operator expressions
# -----------------------------------------------------------------------------

class BinaryOp(Expression):

    def __init__(self, left, right):
        self._left = left
        self._right = right

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right


class Add(BinaryOp):

    def evaluate(self, context):
        lvalue = self.left.evaluate(context)
        rvalue = self.right.evaluate(context)
        return ASTUtil.evaluate_base_type(lvalue + rvalue)


class Subtract(BinaryOp):

    def evaluate(self, context):
        lvalue = self.left.evaluate(context)
        rvalue = self.right.evaluate(context)
        return ASTUtil.evaluate_base_type(lvalue - rvalue)


class Multiply(BinaryOp):

    def evaluate(self, context):
        lvalue = self.left.evaluate(context)
        rvalue = self.right.evaluate(context)
        return ASTUtil.evaluate_base_type(lvalue * rvalue)


class Divide(BinaryOp):

    def evaluate(self, context):
        lvalue = self.left.evaluate(context)
        rvalue = self.right.evaluate(context)
        return ASTUtil.evaluate_base_type(lvalue / rvalue)


class Modulo(BinaryOp):

    def evaluate(self, context):
        lvalue = self.left.evaluate(context)
        rvalue = self.right.evaluate(context)
        return ASTUtil.evaluate_base_type(lvalue % rvalue)


class Power(BinaryOp):

    def evaluate(self, context):
        lvalue = self.left.evaluate(context)
        rvalue = self.right.evaluate(context)
        return ASTUtil.evaluate_base_type(lvalue ** rvalue)


class FloorDivide(BinaryOp):

    def evaluate(self, context):
        lvalue = self.left.evaluate(context)
        rvalue = self.right.evaluate(context)
        return ASTUtil.evaluate_base_type(lvalue // rvalue)


# -----------------------------------------------------------------------------
# Compare operator expressions
# -----------------------------------------------------------------------------

class CompareOp(BinaryOp): pass


class Equal(CompareOp):

    def evaluate(self, context):
        lvalue = self.left.evaluate(context)
        rvalue = self.right.evaluate(context)
        return ASTUtil.evaluate_base_type(lvalue == rvalue)


class NotEqual(CompareOp):

    def evaluate(self, context):
        lvalue = self.left.evaluate(context)
        rvalue = self.right.evaluate(context)
        return ASTUtil.evaluate_base_type(lvalue != rvalue)


class Less(CompareOp):

    def evaluate(self, context):
        lvalue = self.left.evaluate(context)
        rvalue = self.right.evaluate(context)
        return ASTUtil.evaluate_base_type(lvalue < rvalue)


class LessEqual(CompareOp):

    def evaluate(self, context):
        lvalue = self.left.evaluate(context)
        rvalue = self.right.evaluate(context)
        return ASTUtil.evaluate_base_type(lvalue <= rvalue)


class Greater(CompareOp):

    def evaluate(self, context):
        lvalue = self.left.evaluate(context)
        rvalue = self.right.evaluate(context)
        return ASTUtil.evaluate_base_type(lvalue > rvalue)


class GreaterEqual(CompareOp):

    def evaluate(self, context):
        lvalue = self.left.evaluate(context)
        rvalue = self.right.evaluate(context)
        return ASTUtil.evaluate_base_type(lvalue >= rvalue)


# -----------------------------------------------------------------------------
# Atom
# -----------------------------------------------------------------------------

class Atom(Expression):

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def evaluate(self, context):
        return self.value


class Name(Atom):

    def __init__(self, identifier):
        self._identifier = identifier

    @property
    def identifier(self):
        return self._identifier

    def evaluate(self, context):
        identifier = self._identifier
        symbol = context.symtable.lookup(identifier)
        if (not symbol):
            raise RuntimeException(f'{identifier} 未定义')
        node = symbol.node
        return node.evaluate(context)


class Boolean(Atom):

    def evaluate(self, context):
        return ASTUtil.evaluate_base_type(bool(self.value))


class Null(Atom):

    def evaluate(self, context):
        return ASTUtil.evaluate_base_type(None)


class String(Atom):

    def evaluate(self, context):
        return ASTUtil.evaluate_base_type(str(self.value[1:-1]))


class Integer(Atom):

    def evaluate(self, context):
        return ASTUtil.evaluate_base_type(int(self.value))


class Float(Atom):

    def evaluate(self, context):
        return ASTUtil.evaluate_base_type(float(self.value))


class Complex(Atom):

    def evaluate(self, context):
        return ASTUtil.evaluate_base_type(complex(self.value))


# -----------------------------------------------------------------------------
# Iterable
# -----------------------------------------------------------------------------

class Iterable(Atom): pass


# -----------------------------------------------------------------------------
# Tuple
# -----------------------------------------------------------------------------

class Tuple(Iterable):

    def __init__(self, expressions):
        self._expressions = expressions

    @property
    def expressions(self):
        return self._expressions
    
    def evaluate(self, context):
        return ASTUtil.evaluate_base_type(tuple([
            expression.evaluate(context) 
            for expression in self.expressions
        ]))


# -----------------------------------------------------------------------------
# List
# -----------------------------------------------------------------------------

class List(Iterable):

    def __init__(self, expressions):
        self._expressions = expressions

    @property
    def expressions(self):
        return self._expressions
    
    def evaluate(self, context):
        return ASTUtil.evaluate_base_type([
            expression.evaluate(context) 
            for expression in self.expressions
        ])


# -----------------------------------------------------------------------------
# Dictionary
# -----------------------------------------------------------------------------

class Dict(Iterable):

    def __init__(self, kvpairs):
        self._kvpairs = kvpairs

    @property
    def kvpairs(self):
        return self._kvpairs

    def evaluate(self, context):
        the_dict = dict()
        for kvpair in self.kvpairs:
            key, value = kvpair.evaluate(context)
            the_dict[key] = value
        return ASTUtil.evaluate_base_type(the_dict)


class KeyValuePair(Atom):
    
    def __init__(self, expression_key, expression_value):
        self._expression_key = expression_key
        self._expression_value = expression_value

    @property
    def expression_key(self):
        return self._expression_key

    @property
    def expression_value(self):
        return self._expression_value

    def evaluate(self, context):
        key = self.expression_key.evaluate(context)
        value = self.expression_value.evaluate(context)
        return (key, value)


# -----------------------------------------------------------------------------
# Iterable index
# -----------------------------------------------------------------------------

class IterableIndex(Atom):

    def __init__(self, name, expression):
        self._name = name
        self._expression = expression

    @property
    def name(self):
        return self._name

    @property
    def expression(self):
        return self._expression

    def evaluate(self, context):
        iterable = self.name.evaluate(context)
        index = self.expression.evaluate(context)
        return iterable[index]


# -----------------------------------------------------------------------------
# Function call
# -----------------------------------------------------------------------------

class FunctionCall(Atom):

    def __init__(self, primary, arguments):
        self._primary = primary
        self._arguments = arguments

    @property
    def primary(self):
        return self._primary

    @property
    def arguments(self):
        return self._arguments
    
    def evaluate(self, context):
        if (type(self.primary) == ClassMemberCall):
            name = self.primary.traverse(self.primary, context)
            instance = name.evaluate(context)
            self._primary = self.primary.name
            return self.evaluate(instance.context)
        elif (type(self.primary) == Name):
            identifier = self.primary.identifier
            symbol = context.symtable.lookup(identifier)
            if (not symbol):
                raise RuntimeException(f'{identifier} 未定义')
            node = symbol.node

            # Check if calling a class constructor
            if (type(node) == ClassDef):
                return ASTUtil.instantiate_class(context, node)

            # Validate node type
            if (type(node) != FunctionDef):
                raise RuntimeException(f'{identifier} 不是一个函数')

            # Get function definition and its attributes
            functiondef = node
            parameters = functiondef.parameters
            body = functiondef.body

            # Create child context with a new symbol table
            function_symtable = SymbolTable(context.symtable)
            function_context = Context(function_symtable)

            # Insert symbols if default arguments exist
            if (functiondef.default_args):
                for parameter in parameters:
                    arg_identifier = parameter.identifier
                    if (arg_identifier in functiondef.default_args):
                        arg_value = functiondef.default_args[arg_identifier]
                        arg_node = Atom(arg_value)
                        function_context.symtable.insert(
                            arg_identifier, arg_node
                        )
                    else:
                        continue
            
            # Assign expression values to parameters respectively
            for parameter, expression in zip(parameters, self.arguments):
                arg_identifier = parameter.identifier
                arg_node = Atom(expression.evaluate(context))
                function_context.symtable.insert(arg_identifier, arg_node)
            
            # Evaluate function body
            if (callable(body)):
                # Case: built-in function
                function_pointer = body
                args = dict()
                for parameter in parameters:
                    value = parameter.evaluate(function_context)
                    args[parameter.identifier] = value
                return_value = function_pointer(**args)
                return ASTUtil.evaluate_base_type(return_value)
            else:
                # Case: user-defined function
                value = ASTUtil.evaluate_block(
                    function_context, body
                )
                if (type(value).__name__ == 'ReturnValue'):
                    return value
                return ASTUtil.evaluate_base_type(None)


# -----------------------------------------------------------------------------
# Class member call
# -----------------------------------------------------------------------------

class ClassMemberCall(Atom):

    def __init__(self, primary, name):
        self._primary = primary
        self._name = name
    
    @property
    def primary(self):
        return self._primary

    @property
    def name(self):
        return self._name

    def traverse(self, primary, context):
        if (type(primary) == Name):
            return primary
        elif (type(primary) == FunctionCall):
            return primary.evaluate(context)
        else:
            return self.traverse(primary.primary, context)

    def evaluate(self, context):
        name = self.traverse(self.primary, context)
        instance = name.evaluate(context)
        if (type(instance) != ClassType):
            raise RuntimeException(
                f'{self.name.identifier} 不是一个类实例'
            )
        return self.name.evaluate(instance.context)


# -----------------------------------------------------------------------------
# END ast.py
# -----------------------------------------------------------------------------
