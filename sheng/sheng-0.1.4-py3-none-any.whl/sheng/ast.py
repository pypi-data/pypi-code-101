from abc import *
from .symtable import *
from .exception import *
from .builtins import *


class ASTNode(ABC):

    def evaluate(self, symtable):
        raise NotImplementedError()


class ASTUtil(object):

    def evaluate_statements(symtable, sequence):
        for node in sequence:
            value = node.evaluate(symtable)
            if (value):
                return value
        return None

    def evaluate_elifs(symtable, sequence, statements_else=None):
        for expression, statements in sequence:
            if (expression.evaluate(symtable)):
                for node in statements:
                    value = node.evaluate(symtable)
                    if (value):
                        return value
                return None
        if (statements_else):
            return ASTUtil.evaluate_statements(
                symtable, statements_else
            )
        return None


class Program(ASTNode):

    def __init__(self, statements):
        self.statements = statements

    def evaluate(self, symtable):
        return ASTUtil.evaluate_statements(
            symtable, self.statements
        )


class Statement(ASTNode): pass


class FunctionDef(Statement):

    def __init__(self, name, arguments, body):
        self.name = name
        self.arguments = arguments
        self.body = body

    def evaluate(self, symtable):
        identifier = self.name.get_identifier()
        symtable.insert(identifier, self)
        return None

    def get_arguments(self):
        return self.arguments

    def get_body(self):
        return self.body


class Return(Statement):

    def __init__(self, expression):
        self.expression = expression

    def evaluate(self, symtable):
        value = self.expression.evaluate(symtable)
        ReturnValue = type('ReturnValue', (type(value), ), {})
        return ReturnValue(value)


class Assignment(Statement):

    def __init__(self, name, node):
        self.name = name
        self.node = node

    def evaluate(self, symtable):
        identifier = self.name.get_identifier()
        node = Constant(self.node.evaluate(symtable))
        symtable.insert(identifier, node)
        return None


class If(Statement):

    def __init__(self, expression, statements, elifs, statements_else=None):
        self.expression = expression
        self.statements = statements
        self.elifs = elifs
        self.statements_else = statements_else

    def evaluate(self, symtable):
        if (self.expression.evaluate(symtable)):
            return ASTUtil.evaluate_statements(
                symtable, self.statements
            )
        else:
            return ASTUtil.evaluate_elifs(
                symtable, self.elifs, self.statements_else
            )


class Iterate(Statement):

    def __init__(self, variable, iterable, statements):
        self.variable = variable
        self.iterable = iterable
        self.statements = statements

    def evaluate(self, symtable):
        for e in self.iterable.evaluate(symtable):
            node = Constant(e)
            symtable.insert(self.variable, node)
            value = ASTUtil.evaluate_statements(
                symtable, self.statements
            )
            if (type(value).__name__ == 'ReturnValue'):
                return value
            if (type(value).__name__ == 'ContinueValue'):
                continue
            if (type(value).__name__ == 'BreakValue'):
                break
        return None


class Loop(Statement):

    def __init__(self, expression, statements):
        self.expression = expression
        self.statements = statements

    def evaluate(self, symtable):
        while (self.expression.evaluate(symtable)):
            value = ASTUtil.evaluate_statements(
                symtable, self.statements
            )
            if (type(value).__name__ == 'ReturnValue'):
                return value
            if (type(value).__name__ == 'ContinueValue'):
                continue
            if (type(value).__name__ == 'BreakValue'):
                break
        return None


class Continue(Statement):

    def evaluate(self, symtable):
        ContinueValue = type('ContinueValue', (object, ), {})
        return ContinueValue()


class Break(Statement):

    def evaluate(self, symtable):
        BreakValue = type('BreakValue', (object, ), {})
        return BreakValue()


class Expression(ASTNode): pass


class Constant(Expression):

    def __init__(self, value):
        self.value = value

    def evaluate(self, symtable):
        return self.value


class Boolean(Constant):

    def evaluate(self, symtable):
        return BooleanType(self.value)


class Integer(Constant):

    def evaluate(self, symtable):
        return IntegerType(self.value)


class Float(Constant):

    def evaluate(self, symtable):
        return FloatType(self.value)


class Complex(Constant):

    def evaluate(self, symtable):
        return ComplexType(self.value)


class String(Constant):

    def evaluate(self, symtable):
        return StringType(self.value[1:-1])


class UnaryOp(Expression):

    def __init__(self, node):
        self.node = node


class Not(UnaryOp):

    def evaluate(self, symtable):
        value = self.node.evaluate(symtable)
        return not value


class USubtract(UnaryOp):

    def evaluate(self, symtable):
        value = self.node.evaluate(symtable)
        return +value


class UAdd(UnaryOp):

    def evaluate(self, symtable):
        value = self.node.evaluate(symtable)
        return -value


class BinaryOp(Expression):

    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return lvalue + rvalue


class Subtract(BinaryOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return lvalue - rvalue


class Multiply(BinaryOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return lvalue * rvalue


class Divide(BinaryOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return lvalue / rvalue


class Modulo(BinaryOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return lvalue % rvalue


class Power(BinaryOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return lvalue ** rvalue


class FloorDivide(BinaryOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return lvalue // rvalue


class BoolOp(BinaryOp): pass


class And(BoolOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return lvalue and rvalue


class Or(BoolOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return lvalue or rvalue


class CompareOp(BinaryOp): pass


class Equal(CompareOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return lvalue == rvalue


class NotEqual(CompareOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return lvalue != rvalue


class Less(CompareOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return lvalue < rvalue


class LessEqual(CompareOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return lvalue <= rvalue


class Greater(CompareOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return lvalue > rvalue


class GreaterEqual(CompareOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return lvalue >= rvalue


class Name(Expression):

    def __init__(self, value):
        self.value = value

    def get_identifier(self):
        return self.value
    
    def evaluate(self, symtable):
        symbol = symtable.lookup(self.value)
        node = symbol.get_node()
        return node.evaluate(symtable)


class FunctionCall(Expression):

    def __init__(self, name, expressions):
        self.name = name
        self.expressions = expressions
    
    def evaluate(self, symtable):
        identifier = self.name.get_identifier()
        symbol = symtable.lookup(identifier)

        # Validate node type
        if (type(symbol.get_node()) != FunctionDef):
            raise RuntimeException(f'{identifier} is not a function')

        # Get function definition and its attributes
        functiondef = symbol.get_node()
        arguments = functiondef.get_arguments()
        body = functiondef.get_body()

        # Create child symbol table and insert parent symbols
        function_symtable = Function()
        symbols = symtable.to_dict()
        for _, s in symbols.items():
            function_symtable.insert(s.get_identifier(), s.get_node())

        # Validate arguments and expressions size
        if (len(arguments) != len(self.expressions)):
            raise RuntimeException(f'{identifier}, invalid arguments size')
        
        # Assign expression values to arguments respectively
        for argument, expression in zip(arguments, self.expressions):
            arg_identifier = argument.get_identifier()
            arg_node = Constant(expression.evaluate(symtable))
            function_symtable.insert(arg_identifier, arg_node)
        
        # Evaluate function body
        if (type(body) == list):
            # Case: user-defined function
            value = ASTUtil.evaluate_statements(
                function_symtable, body
            )
            if (type(value).__name__ == 'ReturnValue'):
                return value
            return None
        else:
            # Case: built-in function
            function_pointer = body
            args = {}
            for argument in arguments:
                value = argument.evaluate(function_symtable)
                args[argument.get_identifier()] = value
            return function_pointer(**args)


class Iterable(Constant): pass


class List(Iterable):

    def __init__(self, expressions):
        self.expressions = expressions
    
    def evaluate(self, symtable):
        return ListType([
            expression.evaluate(symtable) 
            for expression in self.expressions
        ])


class IterableIndex(Expression):

    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def evaluate(self, symtable):
        iterable = self.name.evaluate(symtable)
        index = self.expression.evaluate(symtable)
        return iterable[index]
