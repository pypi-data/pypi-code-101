from .ply import lex
from .builtins import *
import itertools as _itertools


RESERVED_KEYWORDS = {
    '赋值': 'EQUAL',
    '开始': 'BEGIN',
    '结束': 'END',
    '定义': 'FUNCTIONDEF',
    '返回': 'RETURN',
    '如果': 'IF',
    '则': 'THEN',
    '否则如果': 'ELIF',
    '否则': 'ELSE',
    '对': 'TRUE',
    '错': 'FALSE',
    '与': 'AND',
    '或': 'OR',
    '非': 'NOT',
    '索引': 'INDEX',
    '以': 'FOR',
    '迭代': 'ITERATE',
    '循环': 'LOOP',
    '继续': 'CONTINUE',
    '停止': 'BREAK'
}

EXACT_TOKEN_TYPES = RESERVED_KEYWORDS | {
    ',': 'COMMA',
    '(': 'LPAR',
    ')': 'RPAR',
    '[': 'LSQB',
    ']': 'RSQB',
    '+': 'PLUS',
    '-': 'MINUS',
    '*': 'STAR',
    '/': 'SLASH',
    '**': 'DOUBLESTAR',
    '//': 'DOUBLESLASH',
    '%': 'PERCENT',
    '==': 'EQEQUAL',
    '!=': 'NOTEQUAL',
    '<': 'LESS',
    '<=': 'LESSEQUAL',
    '>': 'GREATER',
    '>=': 'GREATEREQUAL',
    '!': 'NOT'
}

# List of token names.   This is always required
tokens = tuple(set(EXACT_TOKEN_TYPES.values())) + (
    'INTEGER', 'FLOAT', 'COMPLEX', 'STRING', 'NAME'
)

# Regular expression rules for tokens
t_COMMA = r','
t_LPAR = r'\('
t_RPAR = r'\)'
t_LSQB = r'\['
t_RSQB = r'\]'
t_PLUS = r'\+'
t_MINUS = r'-'
t_STAR = r'\*'
t_SLASH = r'/'
t_DOUBLESTAR = r'\*\*'
t_DOUBLESLASH = r'//'
t_PERCENT = r'%'
t_EQEQUAL = r'=='
t_NOTEQUAL = r'!='
t_LESS = r'<'
t_LESSEQUAL = r'<='
t_GREATER = r'>'
t_GREATEREQUAL = r'>='
t_TRUE = r'对'
t_FALSE = r'错'
t_AND = r'与'
t_OR = r'或'
t_NOT = r'(非)|\!'
t_EQUAL = r'赋值'
t_BEGIN = r'开始'
t_END = r'结束'
t_FUNCTIONDEF = r'定义'
t_RETURN = r'返回'
t_IF = r'如果'
t_THEN = r'则'
t_ELIF = r'否则如果'
t_ELSE = r'否则'
t_INDEX = r'索引'
t_FOR = r'以'
t_ITERATE = r'迭代'
t_LOOP = r'循环'
t_CONTINUE = r'继续'
t_BREAK = r'停止'

# Define identifier rule that can only allow chinese characters
def t_NAME(t):
    r'[^\x00-\xff]+'
    if (t.value in RESERVED_KEYWORDS):
        t.type = RESERVED_KEYWORDS[t.value]
    return t

# Define a rule so we can track line numbers
def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1

def group(*choices): return '(' + '|'.join(choices) + ')'
def any(*choices): return group(*choices) + '*'
def maybe(*choices): return group(*choices) + '?'

# Ignore
Whitespace = r'[ \f\t]*'
Comment = r'\#[^\r\n]*'
Ignore = Whitespace + any(r'\\\r?\n' + Whitespace) + maybe(Comment)

t_ignore_COMMENT = Comment
t_ignore = ' \t'

# Number
Hexnumber = r'0[xX](?:_?[0-9a-fA-F])+'
Binnumber = r'0[bB](?:_?[01])+'
Octnumber = r'0[oO](?:_?[0-7])+'
Decnumber = r'(?:0(?:_?0)*|[1-9](?:_?[0-9])*)'
Intnumber = group(Hexnumber, Binnumber, Octnumber, Decnumber)
Exponent = r'[eE][-+]?[0-9](?:_?[0-9])*'
Pointfloat = group(r'[0-9](?:_?[0-9])*\.(?:[0-9](?:_?[0-9])*)?',
                   r'\.[0-9](?:_?[0-9])*') + maybe(Exponent)
Expfloat = r'[0-9](?:_?[0-9])*' + Exponent
Floatnumber = group(Pointfloat, Expfloat)
Imagnumber = group(r'[0-9](?:_?[0-9])*[jJ]', Floatnumber + r'[jJ]')
Number = group(Imagnumber, Floatnumber, Intnumber)

t_INTEGER = Intnumber
t_FLOAT = Floatnumber
t_COMPLEX = Imagnumber

# Return the empty string, plus all of the valid string prefixes.
def _all_string_prefixes():
    # The valid string prefixes. Only contain the lower case versions,
    #  and don't contain any permutations (include 'fr', but not
    #  'rf'). The various permutations will be generated.
    _valid_string_prefixes = ['b', 'r', 'u', 'f', 'br', 'fr']
    # if we add binary f-strings, add: ['fb', 'fbr']
    result = {''}
    for prefix in _valid_string_prefixes:
        for t in _itertools.permutations(prefix):
            # create a list with upper and lower versions of each
            #  character
            for u in _itertools.product(*[(c, c.upper()) for c in t]):
                result.add(''.join(u))
    return result

# Note that since _all_string_prefixes includes the empty string,
#  StringPrefix can be the empty string (making it optional).
StringPrefix = group(*_all_string_prefixes())

# Tail end of ' string.
Single = r"[^'\\]*(?:\\.[^'\\]*)*'"
# Tail end of " string.
Double = r'[^"\\]*(?:\\.[^"\\]*)*"'
# Tail end of ''' string.
Single3 = r"[^'\\]*(?:(?:\\.|'(?!''))[^'\\]*)*'''"
# Tail end of """ string.
Double3 = r'[^"\\]*(?:(?:\\.|"(?!""))[^"\\]*)*"""'
Triple = group(StringPrefix + "'''", StringPrefix + '"""')
# Single-line ' or " string.
String = group(StringPrefix + r"'[^\n'\\]*(?:\\.[^\n'\\]*)*'",
               StringPrefix + r'"[^\n"\\]*(?:\\.[^\n"\\]*)*"')

t_STRING = String

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
