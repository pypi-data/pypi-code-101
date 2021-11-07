from dataclasses import dataclass
from sys import version_info
import typing as t
import types
import dis


@dataclass(init=False, repr=False)
class _Instruction:
    """a mutable instruction"""
    id: int
    opcode: int
    arg: int

    # optional
    jump_target: t.Optional[int]  # target id
    lineno: t.Optional[int]

    def __init__(
        self,
        opcode: int,
        arg: int
    ) -> None:
        self.id = id(self)
        self.opcode = opcode
        self.arg = arg

        self.jump_target = self.lineno = None

    def __repr__(self) -> str:
        return ("Instruction("
                f"{self.id=}, "
                f"{dis.opname[self.opcode]=}, "
                f"{self.arg=}, "
                f"{self.jump_target=}, "
                f"{self.lineno=}"
                ")"
        )

    @classmethod
    def create(cls, ins: dis.Instruction) -> '_Instruction':
        return cls(
            ins.opcode,
            ins.arg or 0
        )


F = t.TypeVar("F", bound=t.Callable[..., t.Any])


def incr(func: F) -> F:
    func.__code__ = patch(func.__code__)
    return func


_pair = {
    "LOAD_NAME": "STORE_NAME",
    "LOAD_GLOBAL": "STORE_GLOBAL",
    "LOAD_FAST": "STORE_FAST",
    "LOAD_ATTR": "STORE_ATTR",
    "LOAD_DEREF": "STORE_DEREF"
}


def patch(code: types.CodeType) -> types.CodeType:
    co_consts = list(code.co_consts)
    instructions = list(_get_instructions(code))

    for i, ins in enumerate(instructions):
        if i >= len(instructions)-2:
            break

        unary_op1, unary_op2 = instructions[i + 1], instructions[i + 2]
        if unary_op1.opcode != unary_op2.opcode:
            continue
        elif dis.opname[unary_op1.opcode] == "UNARY_POSITIVE":
            op_type = "BINARY_ADD"
        elif dis.opname[unary_op1.opcode] == "UNARY_NEGATIVE":
            op_type = "BINARY_SUBTRACT"
        else:
            continue

        opname = dis.opname[ins.opcode]
        if opname not in _pair:
            raise SyntaxError("lvalue required as increment operand."
                              f" at line {_take_min_lineno(instructions, i)}")

        if 1 not in co_consts:
            const_1_i = len(co_consts)
            co_consts.append(1)
        else:
            const_1_i = co_consts.index(1)

        unary_op1.opcode, unary_op1.arg = dis.opmap["LOAD_CONST"], const_1_i
        unary_op2.opcode, unary_op2.arg = dis.opmap[op_type], 0
        instructions.insert(i+3, _Instruction(dis.opmap[_pair[opname]], ins.arg))

        if opname == "LOAD_ATTR":
            instructions.insert(i, _Instruction(dis.opmap["DUP_TOP"], 0))
            i += 1

            instructions.insert(i+3, _Instruction(dis.opmap["ROT_TWO"], 0))
            instructions.insert(i+3, _Instruction(dis.opmap["ROT_THREE"], 0))

        instructions.insert(i+3, _Instruction(dis.opmap["DUP_TOP"], 0))

    if _is_310():
        return code.replace(
            co_code=bytes(_compile(instructions)),
            co_linetable=bytes(_encode_lineno_310(code.co_firstlineno, instructions)),
            co_consts=tuple(co_consts)
        )  # type: ignore

    return code.replace(
        co_code=bytes(_compile(instructions)),
        co_lnotab=bytes(_encode_lineno_39(code.co_firstlineno, instructions)),
        co_consts=tuple(co_consts)
    )


def _is_310() -> bool:
    return version_info[:2] == (3, 10)


def _compile(instructions: t.MutableSequence[_Instruction]) -> t.Generator[int, None, None]:
    """compile sequence of instructions to bytes"""
    # extending args must be done right before compilation
    _extend_args(instructions)
    for i, ins in enumerate(instructions):
        arg = ins.arg
        if ins.opcode in dis.hasjabs:
            target_i, _ = _find_by_id(instructions, ins.jump_target)
            assert target_i != -1
            arg = _get_offset(target_i)
        elif ins.opcode in dis.hasjrel:
            target_i, _ = _find_by_id(instructions, ins.jump_target)
            assert target_i != -1
            target_offset, curr_offset = _get_offset(target_i), _get_offset(i)
            arg = max(target_offset, curr_offset) - 2 - min(target_offset, curr_offset)

        if arg >= 0x100:
            (arg, _), *_ = _split_arg(arg)

        yield from (ins.opcode, arg)


def _extend_args(instructions: t.MutableSequence[_Instruction]) -> None:
    """
    extend the argument of every instructions that is greater than 0xff.
    see https://docs.python.org/3/library/dis.html#opcode-EXTENDED_ARG
    """
    for i, ins in (it := enumerate(instructions)):
        arg = ins.arg
        if ins.opcode in dis.hasjabs:
            target_i, _ = _find_by_id(instructions, ins.jump_target)
            assert target_i != -1
            arg = _get_offset(target_i)
        elif ins.opcode in dis.hasjrel:
            target_i, _ = _find_by_id(instructions, ins.jump_target)
            assert target_i != -1
            target_offset, curr_offset = _get_offset(target_i), _get_offset(i)
            arg = max(target_offset, curr_offset) - 2 - min(target_offset, curr_offset)

        if arg >= 0x100:
            for _, extended_argv in _split_arg(arg):
                instructions.insert(i, _Instruction(dis.opmap["EXTENDED_ARG"], extended_argv))
                next(it)
            last_extended_arg = instructions[i]  # most top EXTENDED_ARG

            jump_referrer = _find_jump_referrer(ins, instructions)
            for referrer_ins in jump_referrer:
                referrer_ins.jump_target = last_extended_arg.id

            # shift lineno
            last_extended_arg.lineno, ins.lineno = ins.lineno, None


def _find_jump_referrer(
    ins: _Instruction,
    instructions: t.Iterable[_Instruction]
) -> t.Iterator[_Instruction]:
    return filter(lambda x: x.jump_target == ins.id, instructions)


def _split_arg(value: int) -> t.Generator[t.Tuple[int, int], None, None]:
    """
    split `value` to three extended_arg argument.
    see https://docs.python.org/3/library/dis.html#opcode-EXTENDED_ARG

    EXTENDED_ARG 1
    JUMP_ABSOLUTE 23

    the first yield value is the remainder value, used in JUMP_ABSOLUTE, and will remain the same.
    the second yield value is extended extended argument, used in EXTENDED_ARG.
    """
    first, value = divmod(value, 0x100)
    second, first = divmod(first, 0x100)
    last, second = divmod(second, 0x100)
    if last >= 0x100:
        raise ValueError(f"too big numbers, max is 32 bit")

    if last:
        yield value, last
    if second:
        yield value, second
    if first:
        yield value, first


def _encode_lineno_39(
    firstlineno: int,
    instructions: t.Iterable[_Instruction]
) -> t.Generator[int, None, None]:
    """encode line number to line number table (co_lnotab)"""
    prevoffset = 0
    prevline = firstlineno
    for i, ins in filter(lambda x: x[1].lineno is not None, enumerate(instructions)):
        ## range offset and range line ##
        # roffset is non-negative, it can be more than 0xff
        # rline can be negative, it is less than or equal to 0xff
        roffset, rline = _get_offset(i)-prevoffset, ins.lineno-prevline

        if roffset >= 0x100:
            # send a PR if you know a more suitable name for 'div' and 'mod'
            div, mod = divmod(roffset, 0xff)
            yield from (0xff, 0) * div
            yield from (mod, 0)
        else:
            yield from (roffset, 0)

        if rline >= 0x80:
            # not fit for half a byte
            div, mod = divmod(rline, 0x7f)
            yield from (0, 0x7f) * div
            yield from (0, mod)
        elif rline < 0:
            yield from (0, 0x100 + rline)
        else:
            yield from (0, rline)

        prevoffset, prevline = _get_offset(i), ins.lineno


def _encode_lineno_310(
    firstlineno: int,
    instructions: t.Sequence[_Instruction]
) -> bytearray:
    # this function is untested...
    # please run the test yourself...
    # make sure you are using python 3.10
    lnotab = bytearray(_encode_lineno_39(firstlineno, instructions))
    # shift offset_incr -1
    i = 0
    while i < len(lnotab)-2:
        lnotab[i] = lnotab[i + 2]
        i += 2
    lnotab[-2] = len(lnotab)
    return lnotab


def _get_instructions(code: types.CodeType) -> t.Generator[_Instruction, None, None]:
    instructions = tuple(map(_Instruction.create, dis.get_instructions(code)))
    if _is_310():
        linemap = dict(map(lambda x: (x[0], x[2]), code.co_lines()))  # type: ignore
    else:
        linemap = dict(dis.findlinestarts(code))

    for i, ins in enumerate(instructions):
        if ins.opcode in dis.hasjabs:
            jump_target_ins = None
            for jump_target_ins in instructions[_get_index(ins.arg):]:
                if dis.opname[jump_target_ins.opcode] != "EXTENDED_ARG":
                    break
            assert jump_target_ins is not None
            ins.jump_target = jump_target_ins.id
        elif ins.opcode in dis.hasjrel:
            jump_target_ins = None
            for jump_target_ins in instructions[_get_index(_get_offset(i) + 2 + ins.arg):]:
                if dis.opname[jump_target_ins.opcode] != "EXTENDED_ARG":
                    break
            assert jump_target_ins is not None
            ins.jump_target = jump_target_ins.id
        elif dis.opname[ins.opcode] == "EXTENDED_ARG":
            offset = _get_offset(i)
            if (lineno := linemap.get(offset, None)) is not None:
                linemap[offset + 2] = lineno
                del linemap[offset]
            continue

        if (lineno := linemap.get(_get_offset(i), None)) is not None:
            ins.lineno = lineno

        yield ins


def _take_min_lineno(instructions: t.Sequence[_Instruction], index: int) -> int:
    if (lineno := instructions[index].lineno) is not None:
        return lineno

    for ins in reversed(instructions[:index]):
        if ins.lineno is not None:
            return ins.lineno
    assert False, "is not working"


def _get_offset(x: int) -> int:
    """
    get offset from index. this function is intended to make it more clear.
    just multiply by 2 since python 3.6 and above always uses 2 bytes for each instructions
    """
    return x * 2


def _get_index(x: int) -> int:
    """
    get index from offset. this function is intended to make it more clear.
    just divide by 2 since python 3.6 and above always uses 2 bytes for each instructions
    """
    return x // 2


def _find_by_id(instructions: t.Iterable[_Instruction], id: int) -> t.Tuple[int, t.Optional[_Instruction]]:
    """find instruction by its id, returns the index and instruction"""
    for i, ins in enumerate(instructions):
        if ins.id == id:
            return i, ins

    return -1, None
