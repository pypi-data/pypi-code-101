"""NanamiLang Fn Handler"""

# This file is a part of NanamiLang Project
# This project licensed under GNU GPL version 2
# Initially made by @jedi2light (aka Stoian Minaiev)

# TODO: pretty unstable implementation, just want to play around

from copy import deepcopy
from functools import reduce
from nanamilang import datatypes


class Fn:
    """NanamiLang Fn Handler"""

    _ev_func = None
    _token_cls = None
    _fn_arg_names: list = None
    _fn_body_form: list = None

    def __init__(self,
                 ev_func,
                 token_cls,
                 fn_arg_names: list,
                 fn_body_token_or_form: list) -> None:
        """NanamiLang Fn Handler, initialize a new instance"""

        self._ev_func = ev_func
        self._token_cls = token_cls
        self._fn_arg_names = fn_arg_names

        self._fn_body_form = [
            token_cls(token_cls.Identifier, 'identity'),
            fn_body_token_or_form
        ] if not isinstance(fn_body_token_or_form, list) else fn_body_token_or_form

    def _from_dt_to_token(self, dt_instance: datatypes.Base):
        """NanamiLang Fn Handler, convert dt instance to token"""

        dt_name = dt_instance.name
        t_type = 'Identifier' if dt_name in ['Undefined', 'Function', 'Macro'] else dt_name

        if isinstance(dt_instance, datatypes.Nil) or isinstance(dt_instance, datatypes.Undefined):
            t_value = dt_instance.origin()
        elif isinstance(dt_instance, datatypes.Macro) or isinstance(dt_instance, datatypes.Function):
            t_value = dt_instance.format()
        else:
            t_value = dt_instance.reference()

        return self._token_cls(t_type, t_value)

    def handle(self, args: list) -> datatypes.Base:
        """NanamiLang Fn Handler, handle function evaluation"""

        for arg in args:
            assert not isinstance(arg, datatypes.Set), 'Fn.handle(): Sets is not supported now :('
            assert not isinstance(arg, datatypes.Vector), 'Fn.handle(): Vectors is not supported now :('
            assert not isinstance(arg, datatypes.HashMap), 'Fn.handle(): HashMaps is not supported now :('

        copied_body_form = deepcopy(self._fn_body_form)

        arg_names_as_tokens = [self._token_cls(self._token_cls.Identifier, x) for x in self._fn_arg_names]
        arg_values_as_tokens = [self._from_dt_to_token(x) for x in args]

        let_bindings_form = list(reduce(lambda e, n: e + n, zip(arg_names_as_tokens, arg_values_as_tokens)))

        return self._ev_func(
            [self._token_cls(self._token_cls.Identifier, 'let'),
             [self._token_cls(self._token_cls.Identifier, 'make-vector')] + let_bindings_form, copied_body_form])
