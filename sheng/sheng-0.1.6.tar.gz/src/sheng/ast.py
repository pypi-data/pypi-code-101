from abc import *
from .symtable import *
from .exception import *
from .builtins import *


# Dictionary from Python built-in types to Sheng BaseType
BASE_TYPE_CLASSES = {
    'NoneType': NullType,
    'bool': BooleanType,
    'int': IntegerType,
    'float': FloatType,
    'complex': ComplexType,
    'str': StringType,
    'tuple': TupleType,
    'list': ListType,
    'dict': DictType
}


class ASTNode(ABC):

    def evaluate(self, symtable):
        raise NotImplementedError()


class ASTUtil(object):

    def evaluate_base_type(value):
        type_name = type(value).__name__
        base_types = [e.__name__ for e in BASE_TYPE_CLASSES.values()]
        if (type_name in base_types):
            return value
        elif (type_name in BASE_TYPE_CLASSES):
            base_type = BASE_TYPE_CLASSES[type_name]
            return base_type(value)
        else:
            raise RuntimeException(
                f'bad operand type: {type_name}'
            )

    def evaluate_statements(symtable, sequence):
        for node in sequence:
            value = node.evaluate(symtable)
            if (value):
                return value
        return None


class Program(ASTNode):

    def __init__(self, statements):
        self.statements = statements

    def evaluate(self, symtable):
        return ASTUtil.evaluate_statements(
            symtable, self.statements
        )


class Statement(ASTNode): pass


class FunctionDef(Statement, BaseType):

    def __init__(self, name, parameters, body):
        super().__init__('函数')
        self.name = name
        self.parameters = parameters
        self.body = body

    def evaluate(self, symtable):
        identifier = self.name.get_identifier()
        symbol = symtable.lookup(identifier)
        if (symbol):
            raise RuntimeException(f'{identifier} has been defined')
        symtable.insert(identifier, self)
        return None

    def get_parameters(self):
        return self.parameters

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

    def __init__(self, expression, statements, statement_elifs, statements_else=None):
        self.expression = expression
        self.statements = statements
        self.statement_elifs = statement_elifs
        self.statements_else = statements_else

    def evaluate(self, symtable):
        if (self.expression.evaluate(symtable)):
            return ASTUtil.evaluate_statements(
                symtable, self.statements
            )
        else:
            for statement_elif in self.statement_elifs:
                if (statement_elif.is_true(symtable)):
                    return statement_elif.evaluate(symtable)
            if (self.statements_else):
                return ASTUtil.evaluate_statements(
                    symtable, self.statements_else
                )
            return None


class Elif(Statement):

    def __init__(self, expression, statements):
        self.expression = expression
        self.statements = statements

    def is_true(self, symtable):
        return self.expression.evaluate(symtable)

    def evaluate(self, symtable):
        for node in self.statements:
            value = node.evaluate(symtable)
            if (value):
                return value
        return None


class Iterate(Statement):

    def __init__(self, variable_identifier, iterable, statements):
        self.variable_identifier = variable_identifier
        self.iterable = iterable
        self.statements = statements

    def evaluate(self, symtable):
        for e in self.iterable.evaluate(symtable):
            node = Constant(e)
            symtable.insert(self.variable_identifier, node)
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
        return ASTUtil.evaluate_base_type(bool(self.value))


class Integer(Constant):

    def evaluate(self, symtable):
        return ASTUtil.evaluate_base_type(int(self.value))


class Float(Constant):

    def evaluate(self, symtable):
        return ASTUtil.evaluate_base_type(float(self.value))


class Complex(Constant):

    def evaluate(self, symtable):
        return ASTUtil.evaluate_base_type(complex(self.value))


class String(Constant):

    def evaluate(self, symtable):
        return ASTUtil.evaluate_base_type(str(self.value[1:-1]))


class Null(Expression):

    def evaluate(self, symtable):
        return ASTUtil.evaluate_base_type(None)


class UnaryOp(Expression):

    def __init__(self, node):
        self.node = node


class Not(UnaryOp):

    def evaluate(self, symtable):
        value = self.node.evaluate(symtable)
        return ASTUtil.evaluate_base_type(not value)


class UAdd(UnaryOp):

    def evaluate(self, symtable):
        value = self.node.evaluate(symtable)
        return ASTUtil.evaluate_base_type(+value)


class USubtract(UnaryOp):

    def evaluate(self, symtable):
        value = self.node.evaluate(symtable)
        return ASTUtil.evaluate_base_type(-value)


class BinaryOp(Expression):

    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return ASTUtil.evaluate_base_type(lvalue + rvalue)


class Subtract(BinaryOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return ASTUtil.evaluate_base_type(lvalue - rvalue)


class Multiply(BinaryOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return ASTUtil.evaluate_base_type(lvalue * rvalue)


class Divide(BinaryOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return ASTUtil.evaluate_base_type(lvalue / rvalue)


class Modulo(BinaryOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return ASTUtil.evaluate_base_type(lvalue % rvalue)


class Power(BinaryOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return ASTUtil.evaluate_base_type(lvalue ** rvalue)


class FloorDivide(BinaryOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return ASTUtil.evaluate_base_type(lvalue // rvalue)


class BoolOp(BinaryOp): pass


class And(BoolOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return ASTUtil.evaluate_base_type(lvalue and rvalue)


class Or(BoolOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return ASTUtil.evaluate_base_type(lvalue or rvalue)


class CompareOp(BinaryOp): pass


class Equal(CompareOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return ASTUtil.evaluate_base_type(lvalue == rvalue)


class NotEqual(CompareOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return ASTUtil.evaluate_base_type(lvalue != rvalue)


class Less(CompareOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return ASTUtil.evaluate_base_type(lvalue < rvalue)


class LessEqual(CompareOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return ASTUtil.evaluate_base_type(lvalue <= rvalue)


class Greater(CompareOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return ASTUtil.evaluate_base_type(lvalue > rvalue)


class GreaterEqual(CompareOp):

    def evaluate(self, symtable):
        lvalue = self.left.evaluate(symtable)
        rvalue = self.right.evaluate(symtable)
        return ASTUtil.evaluate_base_type(lvalue >= rvalue)


class Name(Expression):

    def __init__(self, value):
        self.value = value

    def get_identifier(self):
        return self.value
    
    def evaluate(self, symtable):
        identifier = self.value
        symbol = symtable.lookup(identifier)
        if (not symbol):
            raise RuntimeException(f'{identifier} not defined')
        node = symbol.get_node()
        if (type(node) == FunctionDef):
            return StringType(node.get_type())
        return node.evaluate(symtable)


class FunctionCall(Expression):

    def __init__(self, name, expressions):
        self.name = name
        self.expressions = expressions
    
    def evaluate(self, symtable):
        identifier = self.name.get_identifier()
        symbol = symtable.lookup(identifier)
        if (not symbol):
            raise RuntimeException(f'{identifier} not defined')

        # Validate node type
        if (type(symbol.get_node()) != FunctionDef):
            raise RuntimeException(f'{identifier} is not a function')

        # Get function definition and its attributes
        functiondef = symbol.get_node()
        parameters = functiondef.get_parameters()
        body = functiondef.get_body()

        # Create child symbol table and insert parent symbols
        function_symtable = Function()
        symbols = symtable.to_dict()
        for _, s in symbols.items():
            function_symtable.insert(s.get_identifier(), s.get_node())

        # Validate parameters and expressions size
        if (len(parameters) != len(self.expressions)):
            raise RuntimeException(f'invalid parameters size for {identifier}')
        
        # Assign expression values to parameters respectively
        for parameter, expression in zip(parameters, self.expressions):
            arg_identifier = parameter.get_identifier()
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
            return ASTUtil.evaluate_base_type(None)
        else:
            # Case: built-in function
            function_pointer = body
            args = {}
            for parameter in parameters:
                value = parameter.evaluate(function_symtable)
                args[parameter.get_identifier()] = value
            return_value = function_pointer(**args)
            return ASTUtil.evaluate_base_type(return_value)


class Iterable(Constant): pass


class Tuple(Iterable):

    def __init__(self, expressions):
        self.expressions = expressions
    
    def evaluate(self, symtable):
        return ASTUtil.evaluate_base_type(tuple([
            expression.evaluate(symtable) 
            for expression in self.expressions
        ]))


class List(Iterable):

    def __init__(self, expressions):
        self.expressions = expressions
    
    def evaluate(self, symtable):
        return ASTUtil.evaluate_base_type([
            expression.evaluate(symtable) 
            for expression in self.expressions
        ])


class Dict(Iterable):

    def __init__(self, key_value_pairs):
        self.key_value_pairs = key_value_pairs

    def evaluate(self, symtable):
        the_dict = dict()
        for key_value_pair in self.key_value_pairs:
            key, value = key_value_pair.evaluate(symtable)
            the_dict[key] = value
        return ASTUtil.evaluate_base_type(the_dict)


class KeyValuePair(object):
    
    def __init__(self, expression_key, expression_value):
        self.expression_key = expression_key
        self.expression_value = expression_value

    def evaluate(self, symtable):
        key = self.expression_key.evaluate(symtable)
        value = self.expression_value.evaluate(symtable)
        return (key, value)


class IterableIndex(Expression):

    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def evaluate(self, symtable):
        iterable = self.name.evaluate(symtable)
        index = self.expression.evaluate(symtable)
        return iterable[index]
