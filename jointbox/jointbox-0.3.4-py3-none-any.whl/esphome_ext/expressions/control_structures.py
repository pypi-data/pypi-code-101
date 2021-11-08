#    JointBox CLI
#    Copyright (C) 2021 Dmitry Berezovsky
#    The MIT License (MIT)
#
#    Permission is hereby granted, free of charge, to any person obtaining
#    a copy of this software and associated documentation files
#    (the "Software"), to deal in the Software without restriction,
#    including without limitation the rights to use, copy, modify, merge,
#    publish, distribute, sublicense, and/or sell copies of the Software,
#    and to permit persons to whom the Software is furnished to do so,
#    subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be
#    included in all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#    SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import abc
import copy
import typing
from typing import Dict, Any, Union, Sequence

from cli_rack_validation import crv
from . import const
from ...const import CONF_PARAMS, CONF_NAME

if typing.TYPE_CHECKING:
    from .core import ExpressionEvaluator


class ControlStructuresHandler:
    CONTROL_STRUCTURE_PREFIX = "~"

    def __init__(self) -> None:
        self.handlers = [MacroHandler(), ConditionHandler(), CountHandler(), ForEachHandler()]

    def has_control_structures(self, obj: Dict[str, Any]) -> bool:
        for key in obj.keys():
            if key.startswith(self.CONTROL_STRUCTURE_PREFIX):
                return True
        return False

    def handle(
        self,
        obj: Dict[str, Any],
        parent: Union[Dict[str, Any], Sequence, None],
        parent_idx: Union[str, int, None],
        expressions_evaluator: "ExpressionEvaluator",
    ) -> bool:
        """
        :return: True if expression evaluator should resume processing, false otherwise
        """
        found_handler = False
        resume = True
        for x in self.handlers:
            if x.can_handle(obj):
                found_handler = True
                if (parent is None or parent_idx is None) and not x.supports_root:
                    raise ValueError("Control structure {} is not allowed on the root level".format(x.declaration_name))
                resume = x.handle(obj, parent, parent_idx, expressions_evaluator)
                if not resume:
                    return False
        if not found_handler:
            raise ValueError("Unknown flow control operator")
        return resume


class BaseControlHandler(abc.ABC):
    EXPECT_KEY = ""

    @property
    def declaration_name(self):
        return ControlStructuresHandler.CONTROL_STRUCTURE_PREFIX + self.EXPECT_KEY

    def can_handle(self, obj: Dict[str, Any]):
        return self.declaration_name in obj.keys()

    @property
    def supports_root(self):
        return False

    @abc.abstractmethod
    def handle(
        self,
        obj: Dict[str, Any],
        parent: Union[Dict[str, Any], Sequence, None],
        parent_idx: Union[str, int, None],
        expressions_evaluator: "ExpressionEvaluator",
    ) -> bool:
        pass


class ConditionHandler(BaseControlHandler):
    """
    Syntax variation 1: Evaluate expression in ~if key and if it is FALSE remove whole element from the tree
    Example var. 1:
    data:
        - ~if: a=='1'
          my_data1: 1
          my_data2: 2
    If a != 1 data will be []

    Syntax variation 2: Evaluate epression in ~if key and if it is TRUE replace element with ~then subtree,
    otherwise - replace with ~else subtree if ~else exists or just remove whole element
    Example var 2:
    data:
        ~if: a=='1'
        ~then:
            my_data: 1
        ~else:
            my_data: 2
    """

    EXPECT_KEY = "if"
    _ELSE_KEY = ControlStructuresHandler.CONTROL_STRUCTURE_PREFIX + "else"
    _THEN_KEY = ControlStructuresHandler.CONTROL_STRUCTURE_PREFIX + "then"
    _REPLACE_PARENT = ControlStructuresHandler.CONTROL_STRUCTURE_PREFIX + "replace"

    @property
    def supports_root(self):
        return True

    def _evaluate_branch(self, obj: Dict[str, Any], key: str, evaluator: "ExpressionEvaluator"):
        expr = obj[key]
        if isinstance(expr, str):
            obj[key] = evaluator.process_expression_value(expr)
        elif isinstance(expr, list) or isinstance(expr, dict):
            evaluator.expression_evaluation_pass(expr)

    def _set_parent_val(
        self,
        parent: Union[Dict[str, Any], Sequence, None],
        parent_idx: Union[str, int, None],
        replace_parent: bool,
        new_obj: Any,
    ):
        if not replace_parent:
            parent[parent_idx] = new_obj  # type: ignore
        else:
            if isinstance(parent, dict):
                if isinstance(new_obj, dict):
                    parent.clear()
                    parent.update(new_obj)
                    return
                else:
                    raise ValueError(
                        "An attempt to replace parent element failed due to incompatible types. "
                        "Both parent and ~if evaluation result must be dicts. Got: " + str(new_obj)
                    )
            if isinstance(parent, list):
                if isinstance(new_obj, list):
                    parent.clear()
                    parent += new_obj
                    return
                else:
                    raise ValueError(
                        "An attempt to replace parent element failed due to incompatible types. "
                        "Both parent and ~if evaluation result must be lists. Got: " + str(new_obj)
                    )
            raise ValueError("Unsupported parent node type. Expected either list or dict.")

    def handle(
        self,
        obj: Dict[str, Any],
        parent: Union[Dict[str, Any], Sequence, None],
        parent_idx: Union[str, int, None],
        expressions_evaluator: "ExpressionEvaluator",
    ):
        condition = expressions_evaluator.evaluate_expression(obj[self.declaration_name])
        del obj[self.declaration_name]
        replace_parent = obj.get(self._REPLACE_PARENT, False)
        if self._REPLACE_PARENT in obj:
            del obj[self._REPLACE_PARENT]
        if not condition:
            if self._ELSE_KEY in obj:
                # Syntax variation 2: We have ~else section -> evaluate subtree
                self._evaluate_branch(obj, self._ELSE_KEY, expressions_evaluator)
                # Replace current element with evaluated else block
                self._set_parent_val(parent, parent_idx, replace_parent, obj[self._ELSE_KEY])
            else:
                # If there is not ~else block - just remove self from the tree
                del parent[parent_idx]  # type: ignore
            # Stop further evaluation of this element as it was either already evaluated or removed
            return False
        else:
            if self._THEN_KEY in obj:
                # Syntax variation 2: if ~then key exists then evaluate ~then subtree
                self._evaluate_branch(obj, self._THEN_KEY, expressions_evaluator)
                # Replace current element with evaluated else ~then block
                self._set_parent_val(parent, parent_idx, replace_parent, obj[self._THEN_KEY])
                # Stop further evaluation of this element as it was already evaluated
                return False
        # Syntax variation 1, expression is true -> just continue evaluation
        return True


class BaseLoopHandler(BaseControlHandler, metaclass=abc.ABCMeta):
    def handle(
        self,
        obj: Dict[str, Any],
        parent: Union[Dict[str, Any], Sequence, None],
        parent_idx: Union[str, int, None],
        expressions_evaluator: "ExpressionEvaluator",
    ):
        if not isinstance(parent, list) or not isinstance(parent_idx, int):
            raise ValueError("Loops are available only for list items")
        evaluated_iterator_expr = expressions_evaluator.evaluate_expression(obj[self.declaration_name])
        del obj[self.declaration_name]
        resume = self._validate_iterator(evaluated_iterator_expr)
        if not resume:
            del parent[parent_idx]  # type: ignore
            return False
        result = []
        loop_context = self._create_loop_context()
        template_obj = obj
        parent.pop(parent_idx)
        loop_evaluator = expressions_evaluator.fork(loop_context)
        for it in self._make_iterator(evaluated_iterator_expr):
            self._update_loop_context(it, loop_evaluator.local_context, evaluated_iterator_expr)
            new_obj = copy.deepcopy(template_obj)
            loop_evaluator.expression_evaluation_pass(new_obj)
            result.append(loop_evaluator.mark_evaluated(new_obj))
        insert_index = parent_idx
        for x in result:
            parent.insert(insert_index, x)
            insert_index += 1
        return False

    @classmethod
    def _create_loop_context(cls) -> Dict[str, Any]:
        return {const.CONTEXT_LOOP: {const.CONTEXT_LOOP_CURRENT_INDEX: 0}, const.CONTEXT_LOOP_CURRENT_ELEMENT: None}

    @abc.abstractmethod
    def _update_loop_context(self, current_iterator: Any, context: Dict[str, Any], evaluated_iterator_expr: Any):
        pass

    @abc.abstractmethod
    def _validate_iterator(self, evaluated_expression: Any):
        pass

    @abc.abstractmethod
    def _make_iterator(self, evaluated_expression: Any):
        pass


class CountHandler(BaseLoopHandler):
    EXPECT_KEY = "count"

    def _update_loop_context(self, current_iterator: Any, context: Dict[str, Any], evaluated_iterator_expr: Any):
        context[const.CONTEXT_LOOP][const.CONTEXT_LOOP_CURRENT_INDEX] = current_iterator
        context[const.CONTEXT_LOOP_CURRENT_ELEMENT] = context[const.CONTEXT_LOOP][const.CONTEXT_LOOP_CURRENT_INDEX]

    def _validate_iterator(self, evaluated_expression: Any) -> bool:
        if isinstance(evaluated_expression, int):
            if evaluated_expression < 0:
                raise ValueError("Count value must be positive integer. Got: " + str(evaluated_expression))
            elif evaluated_expression == 0:
                return False
            return True
        else:
            raise ValueError(
                "Count should be integer, representing number of object copies. Got: " + str(evaluated_expression)
            )

    def _make_iterator(self, evaluated_expression: Any):
        return range(evaluated_expression)


class ForEachHandler(BaseLoopHandler):
    EXPECT_KEY = "for_each"

    def _validate_iterator(self, evaluated_expression: Any) -> bool:
        if not isinstance(evaluated_expression, list):
            raise ValueError("for_each operator expects an iterable. Got: " + str(evaluated_expression))
        return len(evaluated_expression) > 0

    def _make_iterator(self, evaluated_expression: Any):
        return enumerate(evaluated_expression)

    def _update_loop_context(self, current_iterator: Any, context: Dict[str, Any], evaluated_iterator_expr: Any):
        idx, it = current_iterator
        context[const.CONTEXT_LOOP][const.CONTEXT_LOOP_CURRENT_INDEX] = idx
        context[const.CONTEXT_LOOP_CURRENT_ELEMENT] = it


class MacroHandler(BaseControlHandler):
    EXPECT_KEY = "macro"

    def handle(
        self,
        obj: Dict[str, Any],
        parent: Union[Dict[str, Any], Sequence, None],
        parent_idx: Union[str, int, None],
        expressions_evaluator: "ExpressionEvaluator",
    ):
        from ..packages.common import MacroDef
        from ..packages.const import CONTEXT_PKG, CONTEXT_VARS

        macro: MacroDef = expressions_evaluator.evaluate_expression(obj[self.declaration_name])
        if not isinstance(macro, MacroDef):
            raise ValueError("Macro must be a valid macro instance. Got: " + str(macro))
        del obj[self.declaration_name]
        # Parse macro params
        with crv.prepend_path(CONF_PARAMS):
            # Validate params
            params = macro.params_validator(obj)
            # Evaluate expressions in params using parent context
            expressions_evaluator.expression_evaluation_pass(params)
        # Create macro evaluation context to evaluate body
        macro_evaluator = expressions_evaluator.fork(
            {
                const.CONTEXT_MACRO: {CONF_PARAMS: params, CONF_NAME: macro.name},
                CONTEXT_PKG: macro.package,
                CONTEXT_VARS: macro.package.meta.variables,
            },
        )
        evaluated_body = copy.deepcopy(macro.body)
        macro_evaluator.expression_evaluation_pass(evaluated_body)
        # Insert result int original object
        parent[parent_idx] = macro_evaluator.mark_evaluated(evaluated_body)  # type: ignore
        return False
