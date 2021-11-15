from .sugarmodule import SugarModule
SugarModule(private_default=True)

from .wrappers import *
from .stubs import *
from ._version import __version__

export(
    SugarModule,
    eat_interrupt,
    eat_arg,
    try_override,
    Partial,
    method_with_attrs,
    FuncNotImplemented,
    NoopStub,
    PassStub,
    StubWrapper,
    PrintStub,
    ErrorStub,
)

meta(
    doc="Syntactical sugar and syntax hack collection for python3",
    author="Misha Klopukh",
    copyright="(c) 2021, Misha Klopukh",
    licence="MIT Licence",
)
