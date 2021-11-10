import pexpect
import re

from sage.rings.integer import Integer
from sage.rings.infinity import PlusInfinity


class Coxeter3:
    def __init__(self, W, q, command="coxeter", timeout=None):
        self._coxeter_group = W
        self._q = q
        self._command = command
        self._timeout = timeout

        if timeout and timeout > 0:
            self._process = pexpect.spawn(command, timeout=timeout)
        else:
            self._process = pexpect.spawn(command, timeout=None)

        cox_matrix = W.coxeter_matrix()
        rank = cox_matrix.rank()

        self._decode_index_set = {cox_i: i for i, cox_i in enumerate(W.index_set(), 1)}
        self._encode_index_set = {v: k for k, v in self._decode_index_set.items()}

        messages = [
            ["coxeter : ", "type"],
            ["type : ", "y"],
            ["rank : ", str(rank)],
        ]

        for message in messages:
            self._process.expect(message[0])
            self._process.sendline(message[1])

        indicies = cox_matrix.index_set()
        for i in range(1, rank):
            coxi = indicies[i - 1]
            for j in range(i + 1, rank + 1):
                coxj = indicies[j - 1]

                self._process.expect("m\\[{},{}\\]".format(str(i), str(j)))
                if (
                    cox_matrix[coxi, coxj] == PlusInfinity()
                    or cox_matrix[coxi, coxj] < 1
                ):
                    self._process.sendline("0")
                else:
                    self._process.sendline(str(cox_matrix[coxi, coxj]))

        messages = [
            ["coxeter : ", "interface"],
            ["interface : ", "terse"],
            ["interface : ", "q"],
        ]

        for message in messages:
            self._process.expect(message[0])
            self._process.sendline(message[1])

    def __ensure_element(self, x):
        if type(x) in [list, tuple]:
            return self._coxeter_group.from_reduced_word(
                [self._encode_index_set[i] for i in x]
            )
        else:
            return x

    def __convert_element_to_coxeter_input(self, element):
        return " ".join(
            [str(self._decode_index_set[i]) for i in element.reduced_word()]
        )

    def __convert_coxeter_output_to_element(self, vals):
        m = re.search("\\[([0-9,]*)\\]", str(vals))
        if m:
            if len(m.group(1)) == 0:
                return self._coxeter_group.one()
            integers = [int(i) for i in m.group(1).split(",")]
            indicies = [self._encode_index_set[i] for i in integers]
            return self._coxeter_group.from_reduced_word(indicies)
        else:
            return None

    def bruhat_interval(self, x, y=None):
        x = self.__ensure_element(x)
        y = self.__ensure_element(y)

        if y is None:
            lower, upper = self._coxeter_group.one(), x
        else:
            lower, upper = x, y

        lower = self.__convert_element_to_coxeter_input(lower)
        upper = self.__convert_element_to_coxeter_input(upper)

        self._process.expect("coxeter : ")
        self._process.sendline("interval")

        self._process.expect("first : ")
        self._process.sendline(lower)

        res = self._process.expect(
            ["second :", "parse error after this : \\(enter new input or ? to abort\\)"]
        )
        if res == 1:
            self._process.sendline("?")
            raise ("Cannot parse word " + lower)

        self._process.sendline(upper)

        res = self._process.expect(
            [
                "Name an output file \\(hit return for stdout\\):",
                "parse error after this : \\(enter new input or ? to abort\\)",
            ]
        )
        if res == 1:
            self._process.sendline("?")
            raise ("Cannot parse word " + upper)

        self._process.sendline("")
        self._process.expect("coxeter : ")

        before = self._process.before
        self._process.sendline("author")

        interval_elements = []

        for line in before.splitlines():
            # try to convert this line into an element
            e = self.__convert_coxeter_output_to_element(line)
            if e:
                interval_elements.append(e)

        return interval_elements

    def klbasis(self, y):
        y = self.__ensure_element(y)

        word = self.__convert_element_to_coxeter_input(y)

        self._process.expect("coxeter : ")
        self._process.sendline("klbasis")
        self._process.expect("enter your element")
        self._process.sendline(word)
        res = self._process.expect(
            [
                "Name an output file \\(hit return for stdout\\):",
                "parse error after this : \\(enter new input or ? to abort\\)",
            ]
        )
        if res == 1:
            self._process.sendline("?")
            raise ("Cannot parse word " + word)
        self._process.sendline("")
        self._process.expect("coxeter : ")

        before = self._process.before
        self._process.sendline("author")

        polynomials = {}

        for line in before.splitlines():
            m = re.search("(\\[[0-9,]*\\]):\\([-0-9,]*\\)\\[([-0-9,]*)\\]", str(line))
            if m:
                e = self.__convert_coxeter_output_to_element(m.group(1))

                pol = []
                if len(m.group(2)) > 0:
                    pol = [Integer(i) for i in m.group(2).split(",")]

                P = self._q.parent().zero()

                for power, coef in enumerate(pol):
                    P = P + coef * (self._q ** power)

                polynomials[e] = P

        return polynomials

    def P(self, x, y):
        x = self.__ensure_element(x)
        y = self.__ensure_element(y)

        if x.bruhat_le(y):
            return self.klbasis(y)[x]
        else:
            raise ("Error 'x' must be less than or equal to 'y' in Bruhat order")
