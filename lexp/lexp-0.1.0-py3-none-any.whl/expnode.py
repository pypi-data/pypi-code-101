import re

from lexp.const import defined_constant
from lexp.exception import ParseError, CalcError
from lexp.funcs import Functions
from lexp.operation.binary import Plus, Minus, Multi, Divide, Power
from lexp.operation.bool import Or, And, Eq, Neq, Ge, Le, Gt, Lt
from lexp.operation.custom import CustomOperation, Variable
from lexp.operation.ternary import EitherOr
from lexp.operation.unary import Not, Negative
from lexp.util import is_number, is_variable_name


class _Part:
    """
    表达式被切分后的组成部分，有上述定义的类型
    """

    def __init__(self, string, t, name=''):
        self.string = string
        self.type = t
        self.name = name

    def __str__(self):
        return self.string


class _Node:
    # 以下为Part类型
    # 函数
    FUNCTION = 1
    # 变量
    VARIABLE = 2
    # 运算符
    OPERATOR = 3
    # 常量
    CONSTANT = 4
    # 括号
    BRACKETS = 5
    # 取负
    NEGATIVE = 6

    def __init__(self, string=''):
        # operation为None，则未解析
        # 此为该节点的运算方式
        self.operation = None

        # 该节点的原始字符串
        self.string = re.sub('[ \r\n\t]', '', string)

        # 参数节点列表，当使用operation进行运算时，将会把所有children带入
        self.children = list()

        # value不为None，则为常量
        self.value = None

    def get_functions(self):
        """
        获得节点中所有函数的信息
        :return: list
        """
        arr = []
        for i in range(0, len(self.children)):
            arr.extend(self.children[i].get_functions())
        if isinstance(self.operation, CustomOperation):
            name = self.operation.name
            if Functions.is_defined(name):
                # lexp预先定义
                t = 'preset'
            else:
                # 用户自行定义
                t = 'custom'
            arr.append({
                'type': t,
                'name': name,
                'minArgc': self.operation.argc
            })
        return arr

    def get_variables(self):
        """
        获得表达式中出现的所有变量
        :return: list
        """
        arr = []
        for i in range(0, len(self.children)):
            child_arr = self.children[i].get_variables()
            for v in child_arr:
                if v not in arr:
                    arr.append(v)
        if isinstance(self.operation, Variable):
            name = self.operation.variable
            if name not in arr:
                arr.append(name)
        return arr

    @staticmethod
    def _get_bracket_position(s):
        """
        最外层括号的位置
        :param s: 字符串
        :return: list
        """
        positions = []
        stack = []
        it = re.finditer('[(]|[)]', s)
        arr = [m.span()[0] for m in it]
        for i in range(0, len(arr)):
            p = arr[i]
            c = s[p:p + 1]
            if c == '(':
                stack.append(p)
            elif c == ')':
                p0 = stack.pop()
                if len(stack) == 0:
                    positions.append((p0, p))
        return positions

    def get_argv(self, string):
        """
        获取字符串参数列表
        :param string: 字符串
        :return: list
        """
        if string == '':
            return []
        # 以最外层括号分块，保持括号中的内容为一个整体
        outer_brackets = self._get_bracket_position(string)
        parts = []
        p = 0
        for i in range(0, len(outer_brackets)):
            bracket_position = outer_brackets[i]
            b0 = bracket_position[0]
            b1 = bracket_position[1]
            if b0 > p:
                parts.append(_Part(string[p:b0], 0))
            parts.append(_Part(string[b0 + 1: b1], self.BRACKETS))
            p = b1 + 1
        if len(string) > p:
            parts.append(_Part(string[p:], 0))
        # 获取以逗号分隔的参数列表，除括号以外
        # argv为参数列表，每一项为part的数组
        argv = []
        # last用作临时存储之前的可能会和后面作为一体的part，比如func与(x+y)
        last = []
        for i in range(0, len(parts)):
            part = parts[i]
            s = part.string
            if part.type == self.BRACKETS:
                last.append(part)
                continue
            ps = [_Part(x, 0) for x in s.split(',')]
            if len(ps) == 1:
                last.append(part)
                continue
            size = len(ps)
            for j in range(0, size):
                p = ps[j]
                if j == 0:
                    if p.string != '':
                        last.append(p)
                    argv.append(last)
                elif j == size - 1:
                    if p.string == '':
                        last = []
                    else:
                        last = [p]
                else:
                    if p.string != '':
                        argv.append([p])
        argv.append(last)
        return argv

    def parse_operation(self, parts):
        """
        解析其中一项参数的字符数组
        :param parts: part list
        :return: None
        """
        characters = []
        for i in range(0, len(parts)):
            p = parts[i]
            s = p.string
            if p.type == self.BRACKETS:
                characters.append(p)
                continue
            it = re.finditer('[-+/*!?:&|=><^]', s)
            position = 0
            for m in it:
                pos = m.span()
                p0 = pos[0]
                p1 = pos[1]
                if p0 > position:
                    characters.append(_Part(s[position:p0], 0))
                characters.append(_Part(s[p0:p1], self.OPERATOR))
                position = p1
            if len(s) > position:
                characters.append(_Part(s[position:len(s)], 0))

        last = None
        arr = []

        def add_single_part(_p):
            if _p is None:
                return
            _c = _p.string
            if _p.type == _Node.BRACKETS:
                arr.append(_Part(_c, _Node.BRACKETS))
            elif is_number(_c):
                arr.append(_Part(_c, _Node.CONSTANT))
            elif is_variable_name(_c):
                arr.append(_Part(_c, _Node.VARIABLE))
            elif _c in ['+', '-', '*', '/', '?', '!', ':', '>', '<', '=', '^']:
                arr.append(_Part(_c, _Node.OPERATOR))
            else:
                # arr.append(_Part(_c, _Node.VARIABLE))
                raise ParseError('wrong charactors %s' % _c)

        # 合并运算符及函数，并给出类型
        for i in range(0, len(characters)):
            p = characters[i]
            c = p.string
            if last is None:
                last_c = None
                last_type = None
            else:
                last_c = last.string
                last_type = last.type

            if p.type == self.BRACKETS and last and is_variable_name(last.string):
                # 前为变量名，后为括号内容，这是一个函数
                arr.append(_Part(c, self.FUNCTION, last_c))
                last = None
            elif last_c == '|' and c == '|':
                arr.append(_Part('||', self.OPERATOR))
                last = None
            elif last_c == '=' and c == '=':
                arr.append(_Part('==', self.OPERATOR))
                last = None
            elif last_c == '!' and c == '=':
                arr.append(_Part('!=', self.OPERATOR))
                last = None
            elif last_c == '&' and c == '&':
                arr.append(_Part('&&', self.OPERATOR))
                last = None
            elif last_c == '>' and c == '=':
                arr.append(_Part('>=', self.OPERATOR))
                last = None
            elif last_c == '<' and c == '=':
                arr.append(_Part('<=', self.OPERATOR))
                last = None
            else:
                if last_type == self.OPERATOR and p.type == self.OPERATOR:
                    allow_repeat_operators = ['!', '-']
                    if c not in allow_repeat_operators and last_c not in allow_repeat_operators:
                        raise ParseError('operator error: %s' % c)
                add_single_part(last)
                last = p
        add_single_part(last)

        # 将符合条件的"-"标为负号
        for i in range(0, len(arr)):
            p = arr[i]
            if p.string == '-':
                if i == 0:
                    p.type = self.NEGATIVE
                elif arr[i - 1].type == self.OPERATOR:
                    p.type = self.NEGATIVE

        # 进一步将组合起来的Part解析为operation和children
        self.parse_single_part(arr)

    def parse_single_part(self, parts):
        """
        递归解析标识好类型的字符数组
        根据parts解析operation和children,形成一个功能完善的Node
        :param parts: part list
        :return: None
        """
        if len(parts) == 1:
            # 只有单个part的情况（常数、变量、括号内容、函数内容）
            p = parts[0]
            if p.type == self.CONSTANT:
                self.value = p.string
            elif p.type == self.VARIABLE:
                self.operation = Variable(p.string)
                self.string = p.string
            # 解析括号
            elif p.type == self.BRACKETS:
                self.string = p.string
                self.parse()
            # 解析函数
            elif p.type == self.FUNCTION:
                self.string = p.string
                self.parse(p.name)
            else:
                raise ParseError('unknown charactor %s' % p.string)
            return
        # 多个part组合的情况
        # 先解析三元运算符
        if self.split_by_ternary(parts):
            return
        # 再解析二元运算符
        if self.split_by_binary(parts):
            return
        # 再解析一元运算符
        if self.split_by_unary(parts):
            return
        # 以上都不是，那么出错了
        arr = [p.string for p in parts]
        raise ParseError('syntax error %s' % ' '.join(arr))

    def split_by_ternary(self, parts):
        """
        解析三元运算符
        只有一种情况: a ? b : c, 三个参数
        :param parts: part list
        :return: True/False
        """
        stack = []
        # 如有多个三元运算符嵌套，取最外层
        for i in range(0, len(parts)):
            p = parts[i]
            if p.type != self.OPERATOR:
                continue
            if p.string == '?':
                stack.append(i)
            elif p.string == ':':
                i0 = stack.pop()
                self.operation = EitherOr()
                condition = _Node()
                condition.parse_single_part(parts[0: i0])

                left = _Node()
                left.parse_single_part(parts[i0 + 1: i])

                right = _Node()
                right.parse_single_part(parts[i + 1:])
                self.children = [condition, left, right]
                return True
        if len(stack) != 0:
            raise ParseError('wrong tertiary operator')
        return False

    def split_by_binary(self, parts):
        """
        解析二元运算符
        :param parts: part list
        :return: True/False
        """
        # 二元运算符优先级(倒序)
        priority = ['||', '&&', '==', '!=', '>=', '<=', '>', '<', '+', '-', '*', '/', '^']
        cls = self.__class__
        for i in range(0, len(priority)):
            symbol = priority[i]
            for j in range(0, len(parts)):
                p = parts[j]
                if p.type != cls.OPERATOR or p.string != symbol:
                    continue
                if symbol == '||':
                    self.operation = Or()
                elif symbol == '&&':
                    self.operation = And()
                elif symbol == '==':
                    self.operation = Eq()
                elif symbol == '!=':
                    self.operation = Neq()
                elif symbol == '>=':
                    self.operation = Ge()
                elif symbol == '<=':
                    self.operation = Le()
                elif symbol == '>':
                    self.operation = Gt()
                elif symbol == '<':
                    self.operation = Lt()
                elif symbol == '+':
                    self.operation = Plus()
                elif symbol == '-':
                    self.operation = Minus()
                elif symbol == '*':
                    self.operation = Multi()
                elif symbol == '/':
                    self.operation = Divide()
                elif symbol == '^':
                    self.operation = Power()
                else:
                    return False
                # 所有二元运算符，一个在左一个在右，两个参数
                left = cls()
                left.parse_single_part(parts[0: j])
                right = cls()
                right.parse_single_part(parts[j + 1:])
                self.children = [left, right]
                return True
        return False

    def split_by_unary(self, parts):
        """
        解析一元运算符
        一元运算符只有两种情况(非、负号)
        :param parts: part list
        :return: Boolean
        """
        n_parts = len(parts)
        for i in range(0, n_parts):
            p = parts[i]
            if p.type == self.OPERATOR and p.string == '!':
                if i >= n_parts - 1:
                    raise ParseError('operator error:!')
                next_p = parts[i + 1]
                self.operation = Not()
                node = _Node()
                node.parse_single_part([next_p])
                self.children.append(node)
                return True
            elif p.type == self.NEGATIVE:
                if i >= n_parts - 1:
                    raise ParseError('operator error:-')
                next_p = parts[i + 1]
                self.operation = Negative()
                node = _Node()
                node.parse_single_part([next_p])
                self.children.append(node)
                return True
        return False

    def parse_children(self, argv):
        """
        解析函数中多项参数
        :param argv: 参数list,每一项为part list
        :return: None
        """
        self.children = []
        for i in range(0, len(argv)):
            parts = argv[i]
            node = _Node()
            node.parse_operation(parts)
            self.children.append(node)

    def parse(self, name=None):
        """
        解析括号或函数中的内容
        :param name: 括号区域的名称，如果没有则为普通括号，有则是函数名
        :return: self
        """
        if not isinstance(self.string, str):
            raise ParseError('no string to parse')
        argv = self.get_argv(self.string)
        if name is None:
            # 普通括号中，不应出现逗号分隔
            if len(argv) > 1:
                raise ParseError('syntax error: %s' % self.string)
            self.parse_operation(argv[0])
        else:
            # 函数中的内容
            if name in Functions.custom_function:
                # 已经注册，归为自定义函数
                self.operation = CustomOperation(name, Functions.custom_function[name])
                self.parse_children(argv)
            elif Functions.is_defined(name.lower()):
                # 在预置函数中有，归为自定义函数
                func = Functions.get_defined(name.lower())
                self.operation = CustomOperation(name, func)
                self.parse_children(argv)
            else:
                raise ParseError(f"unknown function: {name}")
        return self

    @staticmethod
    def _get_variable_value(field, params):
        """
        计算时获取变量的值
        :param field: 变量名
        :param params: calc时传入的params
        :return: float
        """
        if field.lower() in defined_constant:
            val = defined_constant[field.lower()]
            return val
        # 传入的是dict
        if isinstance(params, dict):
            if field not in params:
                # 未传入该变量的值，去预定义常量中查找
                if field.lower() in defined_constant:
                    val = defined_constant[field.lower()]
                    return val
                raise CalcError('not found value of "%s"' % field)
            val = params[field]
            if isinstance(val, str):
                val = float(val)
            return val
        # 传入的是function
        if callable(params):
            return params(field)
        raise CalcError('value error')

    def get_value(self, params):
        """
        calc时，获取该节点的计算结果
        :param params: calc传入的params
        :return: float
        """
        # 此节点为常量，直接取值
        if self.value is not None:
            return float(self.value)

        if self.operation is None:
            raise CalcError('string not parse yet')

        # 此节点为变量，直接获取该变量的值
        if hasattr(self.operation, 'variable'):
            field = self.operation.variable
            return self._get_variable_value(field, params)

        # 获取该节点所有child的值，作为参数带入operation求值
        argv = []
        for i in range(0, len(self.children)):
            val = self.children[i].get_value(params)
            argv.append(val)
        try:
            value = self.operation.operate(argv)
        except CalcError:
            return None
        return value
