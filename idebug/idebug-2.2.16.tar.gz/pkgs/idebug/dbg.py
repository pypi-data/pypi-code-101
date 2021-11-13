# -*- coding: utf-8 -*-
import logging
from datetime import datetime
import os
import re
from copy import copy
import pprint
pp = pprint.PrettyPrinter(indent=2)


__all__ = [
    'logger',
    'funcIdentity',
    'ModuleGubun',
    'PartGubun',
    'SectionGubun',
    'utest',
    'loop',
    'view_dir',
    'view_dict',
    'dictValue',
    'pretty_title',
    'pp',
    'dbg',
    'inspect_mod',
    'inspect_cls',
]


LogLevelDict = {
    10:'DEBUG',
    20:'INFO',
    30:'WARNING',
    40:'ERROR',
    50:'CRITICAL'
}
rLogLevelDict = {v:k for k,v in LogLevelDict.items()}


try:
    LogLevel = os.environ['LOG_LEVEL']
    print(f'사용자 입력 로그 레벨: {LogLevel}')
except Exception as e:
    print(f"""
    ############################################################
                            idebug 셋업상태
    ############################################################
    at {__file__}

    사용자가 로그 레벨을 설정하지 않는다면 기본값은 'DEBUG' 이다.

    원하는 로그 레벨을 설정하고 싶다면,
    1. 코드상에서
    os.environ['LOG_LEVEL'] = '[10/20/.../50/DEBUG/INFO/.../CRITICAL]'
    2. 터미널에서
    export LOG_LEVEL=[10/20...50/DEBUG/INFO/.../CRITICAL]

    상세한 내용은 다음 내용 참조하라.
    https://docs.python.org/3/library/logging.html#logging-levels
    """)
    LogLevel = logging.DEBUG
else:
    try:
        # 사용자 입력갑 청소
        if LogLevel.isnumeric():
            LogLevel = int(LogLevel)
        elif LogLevel.isalpha():
            LogLevel = LogLevel.upper()
            LogLevel = rLogLevelDict[LogLevel]
    except Exception as e:
        print("잘못된 로그 레벨값을 입력했다. 기본값 'DEBUG'로 자동셋업된다.", 'Exception:', e)
        LogLevel = logging.DEBUG
    else:
        pass
finally:
    print('LogLevel:', LogLevel, f'({LogLevelDict[LogLevel]})', type(LogLevel), 'at', __file__)


CommonFormat = "%(asctime)s | %(levelname)s | [%(process)s/%(processName)s][%(thread)s/%(threadName)s]"
MainFormat = f'{CommonFormat} | %(module)s.%(funcName)s[%(lineno)s] | %(message)s'
DecoFormat = f'{CommonFormat} | %(message)s'
# logging.basicConfig(format=MainFormat, level=logging.DEBUG)


"""베이스 로거"""
logger = logging.getLogger('Basic')
logger.setLevel(LogLevel)
# pp.pprint(logger.__dict__)

"""스트림핸들러(터미널에 찍기) 추가"""
sh = logging.StreamHandler()
sh.setLevel(LogLevel)
formatter = logging.Formatter(MainFormat)
sh.setFormatter(formatter)
logger.addHandler(sh)

"""데코레이터 전용 로거"""
decologger = logging.getLogger('Decorator')
decologger.setLevel(LogLevel)
_sh = logging.StreamHandler()
_sh.setLevel(LogLevel)
_formatter = logging.Formatter(DecoFormat)
_sh.setFormatter(_formatter)
decologger.addHandler(_sh)



class Debugger(object):

    def __init__(self):
        self._gubun_len = 100

    @property
    def LogLevel(self):
        return LogLevel

    @property
    def GubunLineLen(self):
        return self._gubun_len

    def set_gubun_len(self, n):
        self._gubun_len = int(n)

    def ModuleGubun(self, _file_):
        print(f"{'@'*self.GubunLineLen} {_file_}")

    def PartGubun(self, s=None, n_newline=5):
        s = 'PartGubun' if s is None else s
        newline = '\n' * n_newline
        logger.debug(f"\n{'='*dbg.GubunLineLen} {s}\n\n")
        print(f"{newline}{'='*dbg.GubunLineLen} {s}")

    def SectionGubun(self, s):
        print(f"\n{'-'*self.GubunLineLen} {s}")

    def pretty_title(self, s, simbol='*', width=None):
        width = self.GubunLineLen if width is None else int(width)
        space = " " * int((width - len(s)) / 2)
        line = simbol * width
        print(f"\n{line}\n{space}{s}{space}\n{line}")

    def dict(self, obj):
        print(f"\n\n{obj.__repr__()}.__dict__")
        pp.pprint(obj.__dict__)
        # title = f"{obj.__repr__()}.__dict__"
        # contents = obj.__dict__
        # logger.debug(f'\n\n\n{title}\n{contents}')

    def dir(self, obj):
        print(f"\n\ndir({obj.__repr__()})")
        pp.pprint(dir(obj))

    def dictValue(self, loc, msg, dic):
        logger.debug(f"{loc} | {msg}")
        pp.pprint(dic)

    def attrs(self, obj):
        self.pretty_title(f'Detail Attrs Info of {obj.__repr__()}')
        for a in dir(obj):
            print(f"{'-'*self.GubunLineLen} {a}")
            v = getattr(obj, a)
            print('type:', type(v))
            print('callable:', callable(v))
            if callable(v):
                try:
                    rv = v()
                except Exception as e:
                    print("Error ->", e)
                else:
                    print('rv ->', rv, type(rv))

dbg = Debugger()


def funcIdentity(f):
    def __funcIdentity(*args, **kwargs):
        fid = f"{f.__module__}.{f.__qualname__}"
        _args = copy(args)[1:]
        _kwargs = kwargs.copy()
        _args = _args if len(_args) > 0 else ''
        _kwargs = _kwargs if len(_kwargs) > 0 else ''
        msg = f'{_args}  {_kwargs}'.strip()
        msg = f'{fid} | {msg}' if len(msg) > 0 else fid
        decologger.debug(msg)

        return f(*args, **kwargs)
    return __funcIdentity


def ModuleGubun(_file_):
    print(f"{'@'*dbg.GubunLineLen} {_file_}")
    logger.debug(f"{'@'*dbg.GubunLineLen} {_file_}")

def PartGubun(partnm=None, viewType=1, n_newline=1, simbol='='):
    partnm = 'PartGubun' if partnm is None else partnm
    gubunline = simbol * dbg.GubunLineLen
    newlines = '\n' * n_newline
    msg = f"\n{gubunline} {partnm}{newlines}"
    if viewType == 1: print(msg)
    elif viewType == 2: logger.debug(msg)
    else: raise

def SectionGubun(sectnm=None, viewType=1, n_newline=0, simbol='-'):
    sectnm = 'SectionGubun' if sectnm is None else sectnm
    gubunline = simbol * dbg.GubunLineLen
    newlines = '\n' * n_newline
    msg = f"\n{gubunline} {sectnm}{newlines}"
    if viewType == 1: print(msg)
    elif viewType == 2: logger.debug(msg)
    else: raise


def _convert_timeunit(seconds):
    sec = 1
    msec = sec / 1000
    min = sec * 60
    hour = min * 60

    t = seconds
    if t < sec:
        unit = 'msec'
        t = t / msec
    elif sec <= t <= min:
        unit = 'secs'
    elif min < t <= hour:
        unit = 'mins'
        t = t / min
    else:
        unit = 'hrs'
        t = t / hour

    return round(t, 1), unit


"""Python decorator 에 대한 공부가 우선이다"""
def utest(f, title=None):
    def _utest(*args, **kwargs):
        print('뭐지?')
        loc = f"{f.__module__}.{f.__qualname__}"
        if len(args) > 1: loc = f"{loc} | {list(args)[1:]}"
        if len(kwargs) > 1: loc = f"{loc} | {kwargs}"
        decologger.debug(msg=loc)

        start_dt = datetime.now()
        # 데코레이터에 주어진 함수 실행
        rv = f(*args, **kwargs)
        # 함수 실행시간 측정
        secs = (datetime.now() - start_dt).total_seconds()
        timeExp, unit = _convert_timeunit(secs)

        decologger.debug(msg=f"{loc} | Runtime: {timeExp} ({unit})")

        return rv
    return _utest


def loop(loc, i, _len, msg=None):
    _msg = f"{loc} {'-'*50} {i}/{_len}"
    msg = _msg if msg is None else f"{_msg} | {msg}"
    logger.debug(msg)


def view_dict(obj, loc=None):
    try:

        loc = '-'*50 if loc is None else loc
        logger.debug(f"{loc} | {obj}.__dict__:")
        pp.pprint(obj.__dict__)
    except Exception as e:
        logger.exception(e)


def view_dir(obj):
    try:
        print(f"\n\n{'-'*50} dir({obj}):")
        pp.pprint(dir(obj))
    except Exception as e:
        logger.exception(e)


def dictValue(loc, msg, dic):
    logger.debug(f"{loc} | {msg}")
    pp.pprint(dic)


def pretty_title(s, simbol='*', width=100):
    space = " " * int((width - len(s)) / 2)
    line = simbol * width
    print(f"\n{line}\n{space}{s}{space}\n{line}")


def _inspect_obj(o, target, linelen, detail=False):
    print(f"type(object): {type(o)}")
    line = '-' * linelen
    p = re.compile('^_')
    elems = dir(o)
    if detail is False:
        elems = [e for e in elems if p.match(e) is None]

    for e in elems:
        a = getattr(o, e)
        _type = type(a)
        _callable = callable(a)
        if _callable:
            try:
                a()
            except Exception as err:
                # v = f"!!!Exception!!! {err}"
                if target == 'func_param':
                    print(line, e)
                    print('type:', _type)
                    print('callable:', _callable)
                    print('Exception -->', err)
            else:
                if target == 'func':
                    rv = a()
                    print(line, e)
                    print('type:', _type)
                    print('callable:', _callable)
                    print('rv -->', rv, type(rv))
        else:
            if target == 'var':
                print(line, e)
                print('type:', _type)
                print('callable:', _callable)
                print(f'{e} -->', a)


def inspect_mod(m, title=None, target='var', linelen=100):
    s = repr(m) if title is None else title
    dbg.pretty_title(s)
    _inspect_obj(m, target, linelen)


def inspect_cls(cls, title=None, target='func', linelen=100):
    s = repr(cls) if title is None else title
    dbg.pretty_title(s)
    _inspect_obj(cls, target, linelen)


class ObjectInspector(object):
    def __init__(self, target='method', linelen=100):
        d = locals()
        del d['self']
        for k,v in d.items():
            setattr(self, k, v)

    def view(self, obj):
        _inspect_obj(obj)
