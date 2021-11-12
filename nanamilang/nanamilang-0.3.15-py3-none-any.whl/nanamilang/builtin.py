"""NanamiLang Builtin Class"""

# This file is a part of NanamiLang Project
# This project licensed under GNU GPL version 2
# Initially made by @jedi2light (aka Stoian Minaiev)

import functools
from typing import List
from functools import reduce
from nanamilang import fn
from nanamilang import datatypes
from nanamilang.shortcuts import randstr
from nanamilang.shortcuts import (
    ASSERT_DICT_CONTAINS_KEY,
    ASSERT_IS_INSTANCE_OF,
    ASSERT_LIST_LENGTH_IS_EVEN,
    ASSERT_COLLECTION_IS_NOT_EMPTY,
    ASSERT_EVERY_COLLECTION_ITEM_IS_INSTANCE_OF
)


class Arity:
    """NanamiLang, builtin.Arity"""
    Even: str = 'Even'
    AtLeastOne: str = 'AtLeastOne'
    LengthVariants: str = 'LengthVariants'
    FunctionAllArgsAre: str = 'FunctionAllArgsAre'
    FunctionAllArgsVariants: str = 'FunctionAllArgsVariants'
    FunctionArgumentsTypeMap: str = 'FunctionArgumentsTypeMap'

    @staticmethod
    def validate(label: str, collection: list, flags: list):
        """NanamiLang Arity.validate() function implementation"""

        for maybe_flag_pair in flags:
            if len(maybe_flag_pair) == 2:
                flag, values = maybe_flag_pair
            else:
                flag, values = maybe_flag_pair[0], None
            if flag == Arity.AtLeastOne:
                ASSERT_COLLECTION_IS_NOT_EMPTY(
                    collection,
                    f'{label}: '
                    f'invalid arity, expected at least one form/argument'
                )
            elif flag == Arity.LengthVariants:
                assert len(collection) in values, (
                    f'{label}: '
                    f'invalid arity, numbers of form(s)/argument(s) possible: {values}'
                )
            elif flag == Arity.FunctionAllArgsAre:
                desired = values[0]
                ASSERT_EVERY_COLLECTION_ITEM_IS_INSTANCE_OF(
                    collection, desired,
                    f'{label}: '
                    f'all function arguments need to be a {desired.name}'
                )
            elif flag == Arity.FunctionAllArgsVariants:
                desired = [v.name for v in values]
                assert len(list(filter(lambda x: x.name in desired,
                                       collection))) == len(collection), (
                    f'{label}: '
                    f'all function arguments need to be either {" or ".join(desired)}'
                )
            elif flag == Arity.FunctionArgumentsTypeMap:
                for [arg, arg_desc] in zip(collection, values):
                    arg_name, arg_type = arg_desc
                    ASSERT_IS_INSTANCE_OF(
                        arg, arg_type, f'{label}: {arg_name} needs to be {arg_type.name}'
                    )
            elif flag == Arity.Even:
                ASSERT_LIST_LENGTH_IS_EVEN(
                    collection,
                    f'{label}: invalid arity, number of function arguments must be even')


def meta(meta_: dict):
    """
    NanamiLang, apply meta to func
    'name': fn/macro LISP name
    'type': 'macro' or 'function'
    'sample': sample fn/macro usage
    'docstring': what fn/macro does

    :param meta_: function meta data
    """

    def wrapped(_fn):
        @functools.wraps(_fn)
        def function(*args, **kwargs):

            arity = meta_.get('arity')
            if arity:
                Arity.validate(meta_.get('name'), list(args[0]), arity)

            return _fn(*args, **kwargs)

        ASSERT_DICT_CONTAINS_KEY('name', meta_, 'function meta data must contain a name')
        ASSERT_DICT_CONTAINS_KEY('type', meta_, 'function meta data must contain a type')
        ASSERT_DICT_CONTAINS_KEY('forms', meta_, 'function meta data must contain a forms')
        ASSERT_DICT_CONTAINS_KEY('docstring', meta_, 'function meta data must contain a docstring')
        function.meta = meta_
        return function

    return wrapped


class BuiltinMacro:
    """NanamiLan Builtin Macro"""

    @staticmethod
    def resolve(mc_name: str) -> dict:
        """Resolve macro by its name"""

        for macro in BuiltinMacro.functions():
            if macro.meta.get('name') == mc_name:
                return {'macro_name': mc_name, 'macro_reference': macro}

    @staticmethod
    def completions() -> List[str]:
        """Return all possible function names (for completion)"""

        _all = BuiltinMacro.functions()

        to_completion = filter(lambda f: not f.meta.get('hidden'), _all)

        return list(map(lambda func: func.meta.get('name'), to_completion))

    @staticmethod
    def names() -> List[str]:
        """Return all possible function names"""

        return list(filter(lambda name: '_macro' in name, BuiltinMacro().__dir__()))

    @staticmethod
    def functions() -> list:
        """Return all possible functions"""

        return list(map(lambda n: getattr(BuiltinMacro, n, None), BuiltinMacro.names()))

    @staticmethod
    def env() -> dict:
        """As 'let' env"""

        variants = [f.meta.get('name') for f in BuiltinMacro.functions()]
        return {n: datatypes.Macro(BuiltinMacro.resolve(n)) for n in variants}

    @staticmethod
    @meta({'arity': [[Arity.LengthVariants, [3]]],
           'name': 'if',
           'type': 'macro',
           'forms': ['(if condition true-branch else-branch)'],
           'docstring': 'Return true- or else-branch depending on condition'})
    def if_macro(tree_slice: list, ev_func, token_cls) -> list:
        """
        Builtin 'if' macro implementation

        :param tree_slice: slice of encountered tree
        :param ev_func: reference to recursive evaluation function
        :param token_cls: nanamilang.token.Token class
        :return: converted slice of tree (as this would be expected)
        """

        condition, true_branch, else_branch = tree_slice

        if not isinstance(condition, list):
            condition = [token_cls(token_cls.Identifier, 'identity'), condition]
        if not isinstance(true_branch, list):
            true_branch = [token_cls(token_cls.Identifier, 'identity'), true_branch]
        if not isinstance(else_branch, list):
            else_branch = [token_cls(token_cls.Identifier, 'identity'), else_branch]

        return true_branch if ev_func(condition).reference() is True else else_branch

    @staticmethod
    @meta({'name': 'comment',
           'type': 'macro',
           'forms': ['(comment ...)'],
           'docstring': 'Turn form into just nothing'})
    def comment_macro(tree_slice: list, ev_func, token_cls) -> list:
        """
        Builtin 'comment' macro implementation

        :param tree_slice: slice of encountered tree
        :param ev_func: reference to recursive evaluation function
        :param token_cls: nanamilang.token.Token class
        :return: converted slice of tree (as this would be expected)
        """

        return [token_cls(token_cls.Identifier, 'identity'), token_cls(token_cls.Nil, 'nil')]

    @staticmethod
    @meta({'arity': [[Arity.AtLeastOne]],
           'name': 'and',
           'type': 'macro',
           'forms': ['(and form1 form2 ... formN)'],
           'docstring': 'Return false if the next cond evaluates to false, otherwise true'})
    def and_macro(tree_slice: list, ev_func, token_cls) -> list:
        """
        Builtin 'and' macro implementation

        :param tree_slice: slice of encountered tree
        :param ev_func: reference to recursive evaluation function
        :param token_cls: nanamilang.token.Token class
        :return: converted slice of tree (as this would be expected)
        """

        for condition in tree_slice:
            if not isinstance(condition, list):
                condition = [token_cls(token_cls.Identifier, 'identity'), condition]
            if ev_func(condition).reference() is False:
                return [token_cls(token_cls.Identifier, 'identity'),
                        token_cls(token_cls.Boolean, False)]
        return [token_cls(token_cls.Identifier, 'identity'), token_cls(token_cls.Boolean, True)]

    @staticmethod
    @meta({'arity': [[Arity.AtLeastOne]],
           'name': 'or',
           'type': 'macro',
           'forms': ['(or form1 form2 ... formN)'],
           'docstring': 'Return true if the next cond evaluates to true, otherwise false'})
    def or_macro(tree_slice: list, ev_func, token_cls) -> list:
        """
        Builtin 'or' macro implementation

        :param tree_slice: slice of encountered tree
        :param ev_func: reference to recursive evaluation function
        :param token_cls: nanamilang.token.Token class
        :return: converted slice of tree (as this would be expected)
        """

        for condition in tree_slice:
            if not isinstance(condition, list):
                condition = [token_cls(token_cls.Identifier, 'identity'), condition]
            if ev_func(condition).reference() is True:
                return [token_cls(token_cls.Identifier, 'identity'),
                        token_cls(token_cls.Boolean, True)]
        return [token_cls(token_cls.Identifier, 'identity'), token_cls(token_cls.Boolean, False)]

    @staticmethod
    @meta({'arity': [[Arity.AtLeastOne]],
           'name': '->',
           'type': 'macro',
           'forms': ['(->  form1 form2 ... formN)'],
           'docstring': 'Allows you to simplify your form'})
    def first_threading_macro(tree_slice: list, ev_func, token_cls) -> list:
        """
        Builtin '->' macro implementation

        :param tree_slice: slice of encountered tree
        :param ev_func: reference to recursive evaluation function
        :param token_cls: nanamilang.token.Token class
        :return: converted slice of tree (as this would be expected)
        """

        if len(tree_slice) > 1:

            for idx, tof in enumerate(tree_slice):
                if len(tree_slice) - 1 != idx:
                    if not isinstance(tof, list):
                        tof = [token_cls(token_cls.Identifier, 'identity'), tof]
                    next_tof = tree_slice[idx + 1]
                    if not isinstance(next_tof, list):
                        tree_slice[idx + 1] = [next_tof, tof]
                    else:
                        tree_slice[idx + 1].insert(1, tof)

            return tree_slice[-1]

        else:

            return [token_cls(token_cls.Identifier, 'identity'), tree_slice[-1]]

    @staticmethod
    @meta({'arity': [[Arity.AtLeastOne]],
           'name': '->>',
           'type': 'macro',
           'forms': ['(->> form1 form2 ... formN)'],
           'docstring': 'Allows you to simplify your form'})
    def last_threading_macro(tree_slice: list, ev_func, token_cls) -> list:
        """
        Builtin '->>' macro implementation

        :param tree_slice: slice of encountered tree
        :param ev_func: reference to recursive evaluation function
        :param token_cls: nanamilang.token.Token class
        :return: converted slice of tree (as this would be expected)
        """

        if len(tree_slice) > 1:

            for idx, tof in enumerate(tree_slice):
                if len(tree_slice) - 1 != idx:
                    if not isinstance(tof, list):
                        tof = [token_cls(token_cls.Identifier, 'identity'), tof]
                    next_tof = tree_slice[idx + 1]
                    if not isinstance(next_tof, list):
                        tree_slice[idx + 1] = [next_tof, tof]
                    else:
                        tree_slice[idx + 1].append(tof)

            return tree_slice[-1]

        else:

            return [token_cls(token_cls.Identifier, 'identity'), tree_slice[-1]]

    @staticmethod
    @meta({'arity': [[Arity.LengthVariants, [2, 3, 4]]],
           'name': 'fn',
           'type': 'macro',
           'forms': ['(fn [n ...] f)',
                     '(fn name [n ...] f)',
                     '(fn "docstring" name [n ...] f)'],
           'docstring': 'Declare your NanamiLang function'})
    def fn_macro(tree_slice: list, ev_func, token_cls) -> list:
        """
        Builtin 'fn' macro implementation

        :param tree_slice: slice of encountered tree
        :param ev_func: reference to recursive evaluation function
        :param token_cls: nanamilang.token.Token class
        :return: converted slice of tree (as this would be expected)
        """

        fn_name_token, fn_docstring_token, fn_arguments_form, fn_body_token_or_form = [None] * 4
        if len(tree_slice) == 2:
            fn_arguments_form, fn_body_token_or_form = tree_slice
        elif len(tree_slice) == 3:
            fn_name_token, fn_arguments_form, fn_body_token_or_form = tree_slice
        elif len(tree_slice) == 4:
            fn_name_token, fn_docstring_token, fn_arguments_form, fn_body_token_or_form = tree_slice

        # Sadly, we can't check that fn_name_token is actually a token, not anything else

        # Sadly, we can't check that fn_docstring_token is actually a token, not anything else

        ASSERT_IS_INSTANCE_OF(fn_arguments_form, list, 'fn: arguments form needs to be a vector')

        but_first = fn_arguments_form[1:]

        fn_argument_names = [t.dt().origin() for t in but_first]

        if fn_name_token:
            fn_name = fn_name_token.dt().origin() or fn_name_token.dt().format()
        else:
            fn_name = randstr()

        fn_handle = fn.Fn(fn_name, ev_func, token_cls, fn_argument_names, fn_body_token_or_form)

        fn_docstring = None
        if fn_docstring_token:
            if fn_docstring_token.type() == 'String':
                fn_docstring = fn_docstring_token.dt().reference()

        Builtin.install(
            {
                'name': fn_name,
                'type': 'function',
                'hidden': not bool(fn_name_token),
                'forms': fn_handle.generate_meta__forms(),
                'docstring': fn_docstring or 'This function has not docstring'
            },
            lambda args: fn_handle.handle(args)
        )

        return [token_cls(token_cls.Identifier, 'identity'), token_cls(token_cls.Identifier, fn_name)]

    @staticmethod
    @meta({'arity': [[Arity.LengthVariants, [1, 2]]],
           'name': 'let',
           'type': 'macro',
           'forms': ['(let [b1 v1 ...] b1)'],
           'docstring': 'Declare your local bindings and access them'})
    def let_macro(tree_slice: list, ev_func, token_cls) -> list:
        """
        Builtin 'let' macro implementation

        :param tree_slice: slice of encountered tree
        :param ev_func: reference to recursive evaluation function
        :param token_cls: nanamilang.token.Token class
        :return: converted slice of tree (as this would be expected)
        """

        # Why on Earth we need to do something if user do not want to use the results?
        if len(tree_slice) == 1:
            return [token_cls(token_cls.Identifier, 'identity'), token_cls(token_cls.Nil, 'nil')]

        bindings_form, body_form = tree_slice

        def token_type_from_dt_instance(dt_instance: datatypes.Base) -> str:
            """
            Return Token.<Something> based on passed data type instance 'name' value
            If data type instance is a Function or a Macro, we will return 'Identifier'
            """
            return token_cls.Identifier if dt_instance.name in ['Function', 'Macro'] else dt_instance.name

        def replace(tof) -> None:
            """
            It will recursively replace tof._type and tof._dt in case
            token bound data type instance is Undefined and we can find its origins in ours local bindings
            """
            if isinstance(tof, list):
                for part in tof:
                    replace(part)
            else:
                if isinstance(tof.dt(), datatypes.Undefined):
                    key = tof.dt().origin()
                    dt: datatypes.Base = env.get(key)
                    if dt is not None:
                        tof.set_type(token_type_from_dt_instance(dt))
                        tof.set_dt(dt)

        # Take care of `bindings_form` form first

        env: dict = {}
        env.update(Builtin.env())
        env.update(BuiltinMacro.env())

        lst = bindings_form[1:]

        # Bindings form must be event to continue
        ASSERT_LIST_LENGTH_IS_EVEN(lst, 'let: bindings form must be even')

        partitioned = [lst[i:i + 2] for i in range(0, len(lst), 2)]

        # Starting from the __first__ element to exclude a 'make-vector' Token.Identifier
        for [key_token, value_token_or_form] in partitioned:
            # --- take care of environment key ---
            # We expect that the `key_token_or_form`:
            # - just a token (not a form, we don't support any kind of destructuring now)
            # - token type is an Identifier (as we can not assign, for example to number)
            # - data type instance assigned to that token is Undefined (no redefinition!)
            if isinstance(key_token, token_cls) and \
                    key_token.type() == token_cls.Identifier and \
                    isinstance(key_token.dt(), datatypes.Undefined):
                env_key = key_token.dt().origin()
            else:
                raise AssertionError(f'let: can\'t assign to: {key_token}')
            # --- take care of environment value ---
            # If `value_or_token_form` is not a list but just a Token instance, wrap it..
            if not isinstance(value_token_or_form, list):
                value_token_or_form = [token_cls(token_cls.Identifier, 'identity'), value_token_or_form]
            # Then, we can try to replace `value_or_token_form` with already filled env..
            replace(value_token_or_form)
            # Then try to evaluate it and update an env
            env[env_key] = ev_func(value_token_or_form)

        # Take care of `body_form` form

        replace(body_form)

        return body_form if isinstance(body_form, list) else [token_cls(token_cls.Identifier, 'identity'), body_form]


class Builtin:
    """NanamiLang Builtin"""

    @staticmethod
    def install(fn_meta: dict, fn_callback) -> bool:
        """
        Allow others to install own functions.
        For example: let the REPL install (exit) function

        Builtin.install() used in current 'fn' implementation

        :param fn_meta: required function meta information
        :param fn_callback: installed function callback reference
        """

        fn_name = fn_meta.get('name')
        reference_key = f'{fn_name}_func'
        maybe_existing = getattr(Builtin, reference_key, None)
        if maybe_existing:
            delattr(Builtin, reference_key)

        setattr(Builtin, reference_key, fn_callback)
        function_attribute = getattr(Builtin, reference_key, None)

        if not function_attribute:
            return False

        function_attribute.meta = fn_meta

        return True

    @staticmethod
    def resolve(fn_name: str) -> dict:
        """Resolve function by its name"""

        for func in Builtin.functions():
            if func.meta.get('name') == fn_name:
                return {'function_name': fn_name, 'function_reference': func}

    @staticmethod
    def completions() -> List[str]:
        """Return all possible function names (for completion)"""

        _all = Builtin.functions()

        to_completion = filter(lambda f: not f.meta.get('hidden'), _all)

        return list(map(lambda func: func.meta.get('name'), to_completion))

    @staticmethod
    def names() -> List[str]:
        """Return all possible function names"""

        return list(filter(lambda name: '_func' in name, Builtin().__dir__()))

    @staticmethod
    def functions() -> list:
        """Return all possible functions"""

        return list(map(lambda n: getattr(Builtin, n, None), Builtin.names()))

    @staticmethod
    def env() -> dict:
        """As 'let' env"""

        variants = [f.meta.get('name') for f in Builtin.functions()]
        return {n: datatypes.Function(Builtin.resolve(n)) for n in variants}

    @staticmethod
    @meta({'arity': [[Arity.LengthVariants, [1]],
                     [Arity.FunctionAllArgsAre, [datatypes.String]]],
           'name': 'find-mc',
           'type': 'function',
           'forms': ['(find-mc mc-name)'],
           'docstring': 'Find a Macro by its name'})
    def find_mc_func(args: List[datatypes.String]) -> datatypes.Macro or datatypes.Nil:
        """
        Builtin 'find-mc' function implementation

        :param args: incoming 'find-mc' function arguments
        :return: datatypes.Macro or datatypes.Nil
        """

        macro_name_as_string: datatypes.String = args[0]

        resolved_macro_info = BuiltinMacro.resolve(macro_name_as_string.reference())

        return datatypes.Macro(resolved_macro_info) if resolved_macro_info else datatypes.Nil('nil')

    @staticmethod
    @meta({'arity': [[Arity.LengthVariants, [1]],
                     [Arity.FunctionAllArgsAre, [datatypes.String]]],
           'name': 'find-fn',
           'type': 'function',
           'forms': ['(find-fn fn-name)'],
           'docstring': 'Find a Function by its name'})
    def find_fn_func(args: List[datatypes.String]) -> datatypes.Function or datatypes.Nil:
        """
        Builtin 'find-fn' function implementation

        :param args: incoming 'find-fn' function arguments
        :return: datatypes.Function or datatypes.Nil
        """

        function_name_as_string: datatypes.String = args[0]

        resolved_function_info = Builtin.resolve(function_name_as_string.reference())

        return datatypes.Function(resolved_function_info) if resolved_function_info else datatypes.Nil('nil')

    @staticmethod
    @meta({'arity': [[Arity.LengthVariants, [1]],
                     [Arity.FunctionAllArgsVariants, [datatypes.Macro,
                                                      datatypes.Function]]],
           'name': 'doc',
           'type': 'function',
           'forms': ['(doc function-or-macro)'],
           'docstring': 'Function or Macro documentation'})
    def doc_func(args: List[datatypes.Function or datatypes.Macro]) -> datatypes.HashMap:
        """
        Builtin 'doc' function implementation

        :param args: incoming 'doc' function arguments
        :return: datatypes.HashMap
        """

        function_or_macro: datatypes.Function or datatypes.Macro = args[0]

        _type = function_or_macro.reference().meta.get('type')

        return Builtin.make_hashmap_func([datatypes.Keyword('forms'),
                                          Builtin.make_vector_func(
                                              [datatypes.String(x)
                                               for x in function_or_macro.reference().meta.get('forms')]
                                          ),
                                          datatypes.Keyword('macro?'), datatypes.Boolean(_type == 'macro'),
                                          datatypes.Keyword('function?'), datatypes.Boolean(_type == 'function'),
                                          datatypes.Keyword('docstring'),
                                          datatypes.String(function_or_macro.reference().meta.get('docstring'))])

    @staticmethod
    @meta({'arity': [[Arity.LengthVariants, [2]]],
           'name': 'get',
           'type': 'function',
           'forms': ['(get collection key-or-index)'],
           'docstring': 'A collection item by its key or index'})
    def get_func(args: List[datatypes.Base]) -> datatypes.Base:
        """
        Builtin 'get' function implementation

        :param args: incoming 'get' function arguments
        :return: datatypes.Base
        """

        collection: datatypes.Vector or datatypes.HashMap
        key_or_index: datatypes.Base

        collection, key_or_index = args

        assert (isinstance(collection, datatypes.Vector)
                or isinstance(collection, datatypes.HashMap)), (
            'get: collection needs to be either HashMap or Vector'
        )

        # Let the collection.get() handle whether key_or_index is of right type or not

        return collection.get(key_or_index)

    @staticmethod
    @meta({'arity': [[Arity.LengthVariants, [2]],
                     [Arity.FunctionArgumentsTypeMap, [['function', datatypes.Function],
                                                       ['collection', datatypes.Vector]]]],
           'name': 'map',
           'type': 'function',
           'forms': ['(map function collection)'],
           'docstring': 'A Vector of mapped collection items'})
    def map_func(args: List[datatypes.Base]) -> datatypes.Vector:
        """
        Builtin 'map' function implementation

        :param args: incoming 'map' function arguments
        :return: datatypes.Vector
        """

        function: datatypes.Function
        collection: datatypes.Vector

        function, collection = args

        return datatypes.Vector(list(map(lambda e: function.reference()([e]), collection.reference())))

    @staticmethod
    @meta({'arity': [[Arity.LengthVariants, [2]],
                     [Arity.FunctionArgumentsTypeMap, [['function', datatypes.Function],
                                                       ['collection', datatypes.Vector]]]],
           'name': 'filter',
           'type': 'function',
           'forms': ['(filter function collection)'],
           'docstring': 'A Vector of filtered collection items'})
    def filter_func(args: List[datatypes.Base]) -> datatypes.Vector:
        """
        Builtin 'filter' function implementation

        :param args: incoming 'filter' function arguments
        :return: datatypes.Vector
        """

        function: datatypes.Function
        collection: datatypes.Vector

        function, collection = args

        return datatypes.Vector(
            list(filter(lambda e: function.reference()([e]).reference() is True, collection.reference())))

    @staticmethod
    @meta({'name': 'make-set',
           'type': 'function',
           'forms': ['(make-set e1 e2 ... eX)'],
           'docstring': 'Create a Set data structure'})
    def make_set_func(args: List[datatypes.Base]) -> datatypes.Set:
        """
        Builtin 'make-set' function implementation

        :param args: incoming 'make-set' function arguments
        :return: datatypes.Set
        """

        return datatypes.Set(set(args))

    @staticmethod
    @meta({'name': 'make-vector',
           'type': 'function',
           'forms': ['(make-vector e1 e2 ... eX)'],
           'docstring': 'Create a Vector data structure'})
    def make_vector_func(args: List[datatypes.Base]) -> datatypes.Vector:
        """
        Builtin 'make-vector' function implementation

        :param args: incoming 'make-vector' function arguments
        :return: datatypes.Vector
        """

        return datatypes.Vector(list(args))

    @staticmethod
    @meta({'arity': [[Arity.Even]],
           'name': 'make-hashmap',
           'type': 'function',
           'forms': ['(make-hashmap k1 v2 ... kX vX)'],
           'docstring': 'Create a HashMap data structure'})
    def make_hashmap_func(args: List[datatypes.Base]) -> datatypes.HashMap:
        """
        Builtin 'make-hashmap' function implementation

        :param args: incoming 'make-hashmap' function arguments
        :return: datatypes.HashMap
        """

        return datatypes.HashMap(dict({k: v for [k, v] in [args[i:i + 2] for i in range(0, len(args), 2)]}))

    @staticmethod
    @meta({'arity': [[Arity.LengthVariants, [1]],
                     [Arity.FunctionAllArgsVariants, [datatypes.IntegerNumber,
                                                      datatypes.FloatNumber]]],
           'name': 'inc',
           'type': 'function',
           'forms': ['(inc number)'],
           'docstring': 'Return incremented number'})
    def inc_func(args: (List[datatypes.IntegerNumber]
                        or List[datatypes.FloatNumber])) -> (datatypes.IntegerNumber
                                                             or datatypes.FloatNumber):
        """
        Builtin 'inc' function implementation

        :param args: incoming 'inc' function arguments
        :return: datatypes.IntegerNumber or datatypes.FloatNumber
        """

        number: (datatypes.IntegerNumber or datatypes.FloatNumber) = args[0]

        return datatypes.IntegerNumber(number.reference() + 1) if \
            isinstance(number, datatypes.IntegerNumber) else datatypes.FloatNumber(number.reference() + 1)

    @staticmethod
    @meta({'arity': [[Arity.LengthVariants, [1]],
                     [Arity.FunctionAllArgsVariants, [datatypes.IntegerNumber,
                                                      datatypes.FloatNumber]]],
           'name': 'dec',
           'type': 'function',
           'forms': ['(dec number)'],
           'docstring': 'Return decremented number'})
    def dec_func(args: (List[datatypes.IntegerNumber]
                        or List[datatypes.FloatNumber])) -> (datatypes.IntegerNumber
                                                             or datatypes.FloatNumber):
        """
        Builtin 'dec' function implementation

        :param args: incoming 'dec' function arguments
        :return: datatypes.IntegerNumber or datatypes.FloatNumber
        """

        number: (datatypes.IntegerNumber or datatypes.FloatNumber) = args[0]

        return datatypes.IntegerNumber(number.reference() - 1) if \
            isinstance(number, datatypes.IntegerNumber) else datatypes.FloatNumber(number.reference() - 1)

    @staticmethod
    @meta({'arity': [[Arity.LengthVariants, [1]]],
           'name': 'identity',
           'type': 'function',
           'forms': ['(identity something)'],
           'docstring': 'Just return a something'})
    def identity_func(args: List[datatypes.Base]) -> datatypes.Base:
        """
        Builtin 'identity' function implementation

        :param args: incoming 'identity' function arguments
        :return: datatypes.Base
        """

        something: datatypes.Base = args[0]

        return something

    @staticmethod
    @meta({'arity': [[Arity.LengthVariants, [1]]],
           'name': 'type',
           'type': 'function',
           'forms': ['(type something)'],
           'docstring': 'Just return something type name'})
    def type_func(args: List[datatypes.Base]) -> datatypes.String:
        """
        Builtin 'type' function implementation

        :param args: incoming 'type' function arguments
        :return: datatypes.String
        """

        something: datatypes.Base = args[0]

        return datatypes.String(something.name)

    @staticmethod
    @meta({'arity': [[Arity.LengthVariants, [2]]],
           'name': '=',
           'type': 'function',
           'forms': ['(= f s)'],
           'docstring': 'Whether f equals to s or not'})
    def eq_func(args: List[datatypes.Base]) -> datatypes.Boolean:
        """
        Builtin '=' function implementation

        :param args: incoming '=' function arguments
        :return: datatypes.Boolean
        """

        # TODO: maybe refactor this function to support more than two arguments and use overloaded operators

        f: datatypes.Base
        s: datatypes.Base
        f, s = args

        return datatypes.Boolean(f.reference() == s.reference())

    @staticmethod
    @meta({'arity': [[Arity.LengthVariants, [2]],
                     [Arity.FunctionAllArgsVariants, [datatypes.IntegerNumber,
                                                      datatypes.FloatNumber]]],
           'name': '<',
           'type': 'function',
           'forms': ['(< f s)'],
           'docstring': 'Whether f lower than s or not'})
    def lower_than_func(args: (List[datatypes.IntegerNumber]
                               or List[datatypes.FloatNumber])) -> datatypes.Boolean:
        """
        Builtin '<' function implementation

        :param args: incoming '<' function arguments
        :return: datatypes.Boolean
        """

        # TODO: maybe refactor this function to support more than two arguments and use overloaded operators

        f: datatypes.IntegerNumber or datatypes.FloatNumber
        s: datatypes.IntegerNumber or datatypes.FloatNumber
        f, s = args

        return datatypes.Boolean(f.reference() < s.reference())

    @staticmethod
    @meta({'arity': [[Arity.LengthVariants, [2]],
                     [Arity.FunctionAllArgsVariants, [datatypes.IntegerNumber,
                                                      datatypes.FloatNumber]]],
           'name': '>',
           'type': 'function',
           'forms': ['(> f s)'],
           'docstring': 'Whether f greater than s or not'})
    def greater_than_func(args: (List[datatypes.IntegerNumber]
                                 or List[datatypes.FloatNumber])) -> datatypes.Boolean:
        """
        Builtin '>' function implementation

        :param args: incoming '>' function arguments
        :return: datatypes.Boolean
        """

        # TODO: maybe refactor this function to support more than two arguments and use overloaded operators

        f: datatypes.IntegerNumber or datatypes.FloatNumber
        s: datatypes.IntegerNumber or datatypes.FloatNumber
        f, s = args

        return datatypes.Boolean(f.reference() > s.reference())

    @staticmethod
    @meta({'arity': [[Arity.LengthVariants, [2]],
                     [Arity.FunctionAllArgsVariants, [datatypes.IntegerNumber,
                                                      datatypes.FloatNumber]]],
           'name': '<=',
           'type': 'function',
           'forms': ['(<= f s)'],
           'docstring': 'Whether f lower than or equals to s or not'})
    def lower_than_eq_func(args: (List[datatypes.IntegerNumber]
                                  or List[datatypes.FloatNumber])) -> datatypes.Boolean:
        """
        Builtin '<=' function implementation

        :param args: incoming '>=' function arguments
        :return: datatypes.Boolean
        """

        # TODO: maybe refactor this function to support more than two arguments and use overloaded operators

        f: datatypes.IntegerNumber or datatypes.FloatNumber
        s: datatypes.IntegerNumber or datatypes.FloatNumber
        f, s = args

        return datatypes.Boolean(f.reference() <= s.reference())

    @staticmethod
    @meta({'arity': [[Arity.LengthVariants, [2]],
                     [Arity.FunctionAllArgsVariants, [datatypes.IntegerNumber,
                                                      datatypes.FloatNumber]]],
           'name': '>=',
           'type': 'function',
           'forms': ['(>= f s)'],
           'docstring': 'Whether f greater than or equals to s or not'})
    def greater_than_eq_func(args: (List[datatypes.IntegerNumber]
                                    or List[datatypes.FloatNumber])) -> datatypes.Boolean:
        """
        Builtin '>=' function implementation

        :param args: incoming '>=' function arguments
        :return: datatypes.Boolean
        """

        # TODO: maybe refactor this function to support more than two arguments and use overloaded operators

        f: datatypes.IntegerNumber or datatypes.FloatNumber
        f: datatypes.IntegerNumber or datatypes.FloatNumber
        f, s = args

        return datatypes.Boolean(f.reference() >= s.reference())

    @staticmethod
    @meta({'arity': [[Arity.AtLeastOne],
                     [Arity.FunctionAllArgsVariants, [datatypes.IntegerNumber,
                                                      datatypes.FloatNumber]]],
           'name': '+',
           'type': 'function',
           'forms': ['(+ n1 n2 ... nX)'],
           'docstring': 'All passed numbers summary'})
    def plus_func(args: (List[datatypes.IntegerNumber]
                         or List[datatypes.FloatNumber])) -> (datatypes.IntegerNumber
                                                              or datatypes.FloatNumber):
        """
        Builtin '+' function implementation

        :param args: incoming '+' function arguments
        :return: datatypes.IntegerNumber or datatypes.FloatNumber
        """

        result = reduce(lambda _, x: _ + x, list(map(lambda n: n.reference(), args)))

        return datatypes.IntegerNumber(result) if isinstance(result, int) else datatypes.FloatNumber(result)

    @staticmethod
    @meta({'arity': [[Arity.AtLeastOne],
                     [Arity.FunctionAllArgsVariants, [datatypes.IntegerNumber,
                                                      datatypes.FloatNumber]]],
           'name': '-',
           'type': 'function',
           'forms': ['(- n1 n2 ... nX)'],
           'docstring': 'All passed numbers subtraction'})
    def minus_func(args: (List[datatypes.IntegerNumber]
                          or List[datatypes.FloatNumber])) -> (datatypes.IntegerNumber
                                                               or datatypes.FloatNumber):
        """
        Builtin '-' function implementation

        :param args: incoming '-' function arguments
        :return: datatypes.IntegerNumber or datatypes.FloatNumber
        """

        result = reduce(lambda _, x: _ - x, list(map(lambda n: n.reference(), args)))

        return datatypes.IntegerNumber(result) if isinstance(result, int) else datatypes.FloatNumber(result)

    @staticmethod
    @meta({'arity': [[Arity.AtLeastOne],
                     [Arity.FunctionAllArgsVariants, [datatypes.IntegerNumber,
                                                      datatypes.FloatNumber]]],
           'name': '/',
           'type': 'function',
           'forms': ['(/ n1 n2 ... nX)'],
           'docstring': 'All passed numbers division'})
    def divide_func(args: (List[datatypes.IntegerNumber]
                           or List[datatypes.FloatNumber])) -> (datatypes.IntegerNumber
                                                                or datatypes.FloatNumber):
        """
        Builtin '/' function implementation

        :param args: incoming '/' function arguments
        :return: datatypes.IntegerNumber or datatypes.FloatNumber
        """

        result = reduce(lambda _, x: _ / x, list(map(lambda n: n.reference(), args)))

        return datatypes.IntegerNumber(result) if isinstance(result, int) else datatypes.FloatNumber(result)

    @staticmethod
    @meta({'arity': [[Arity.AtLeastOne],
                     [Arity.FunctionAllArgsVariants, [datatypes.IntegerNumber,
                                                      datatypes.FloatNumber]]],
           'name': '*',
           'type': 'function',
           'forms': ['(* n1 n2 ... nX)'],
           'docstring': 'All passed numbers production'})
    def multiply_func(args: (List[datatypes.IntegerNumber]
                             or List[datatypes.FloatNumber])) -> (datatypes.IntegerNumber
                                                                  or datatypes.FloatNumber):
        """
        Builtin '*' function implementation

        :param args: incoming '*' function arguments
        :return: datatypes.IntegerNumber or datatypes.FloatNumber
        """

        result = reduce(lambda _, x: _ * x, list(map(lambda n: n.reference(), args)))

        return datatypes.IntegerNumber(result) if isinstance(result, int) else datatypes.FloatNumber(result)

    @staticmethod
    @meta({'arity': [[Arity.AtLeastOne],
                     [Arity.FunctionAllArgsVariants, [datatypes.IntegerNumber,
                                                      datatypes.FloatNumber]]],
           'name': 'mod',
           'type': 'function',
           'forms': ['(mod n1 n2 ... nX)'],
           'docstring': 'All passed numbers modification'})
    def mod_func(args: (List[datatypes.IntegerNumber]
                        or List[datatypes.FloatNumber])) -> (datatypes.IntegerNumber
                                                             or datatypes.FloatNumber):
        """
        Builtin 'mod' function implementation

        :param args: incoming 'mod' function arguments
        :return: datatypes.IntegerNumber or datatypes.FloatNumber
        """

        result = reduce(lambda _, x: _ % x, list(map(lambda n: n.reference(), args)))

        return datatypes.IntegerNumber(result) if isinstance(result, int) else datatypes.FloatNumber(result)
