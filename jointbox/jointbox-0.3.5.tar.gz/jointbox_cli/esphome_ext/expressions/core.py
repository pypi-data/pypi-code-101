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

import copy
from typing import Optional, Union, Any, Dict, Sequence
from cli_rack_validation import crv
from .common import TreeItem, TreePath, ControlCommand, UNDEFINED, RESET_ITERATION
from .control_structures import ControlStructuresHandler

from ..expressions import process_expression_value, TemplateRenderingError, evaluate_expression, unwrap_expression


class EvaluatedObject(dict):
    def __init__(self, data: dict) -> None:
        super().__init__(data)


class ExpressionEvaluator(object):
    EVALUATION_APPLIED = "_evaluation_applied"

    def __init__(self) -> None:
        self.local_context: Dict[str, Any] = {}
        self._path: TreePath = []
        self.control_structures_handler = ControlStructuresHandler()

    def copy(self) -> "ExpressionEvaluator":
        inst = self.__class__()
        inst.local_context = copy.copy(self.local_context)
        inst._path = copy.copy(self._path)
        inst.control_structures_handler = self.control_structures_handler
        return inst

    def fork(self, extra_context: Dict[str, Any]) -> "ExpressionEvaluator":
        inst = self.copy()
        inst.local_context.update(extra_context)
        return inst

    def expression_evaluation_pass(self, val: Union[dict, list]):
        self._evaluate_expressions_for_item(val, self._path, None)

    def mark_evaluated(self, obj: Union[list, dict]) -> Any:
        if isinstance(obj, dict):
            return EvaluatedObject(obj)
        else:
            result = []
            for x in obj:
                if isinstance(obj, dict):
                    result.append(EvaluatedObject(x))
                else:
                    result.append(x)
            return result

    def is_already_evaluated(self, obj: Any) -> bool:
        return isinstance(obj, EvaluatedObject)

    def _evaluate_expressions_for_item(  # noqa: C901
        self, val: TreeItem, path: TreePath, parent: Optional[Union[Sequence, Dict]]
    ) -> Optional[Union[TreeItem, ControlCommand]]:
        # Walk the three recursively
        if isinstance(val, dict):
            if self.control_structures_handler.has_control_structures(val):
                try:
                    resume_processing = self.control_structures_handler.handle(
                        val, parent, path[-1] if len(path) > 0 else None, self
                    )
                    if not resume_processing:
                        return RESET_ITERATION if isinstance(parent, list) else UNDEFINED
                except Exception as e:
                    raise crv.Invalid(str(e), path)
            for k, v in list(val.items()):
                res = self._evaluate_expressions_for_item(v, path + [k], val)
                if not isinstance(res, ControlCommand):
                    val[k] = res
        elif isinstance(val, list):
            reset_iteration = False
            while True:
                reset_iteration = False
                for i, it in enumerate(val):
                    if self.is_already_evaluated(it):
                        continue
                    res = self._evaluate_expressions_for_item(it, path + [i], val)
                    if not isinstance(res, ControlCommand):
                        val[i] = res
                    if res == RESET_ITERATION:
                        reset_iteration = True
                        break
                if not reset_iteration:
                    break
        elif isinstance(val, str):
            try:
                return self.process_expression_value(val)
            except TemplateRenderingError as e:
                raise crv.Invalid(str(e), path)

        return UNDEFINED

    def process_expression_value(self, value):
        unwrapped = unwrap_expression(value)
        if unwrapped is not None:
            return self.evaluate_expression(unwrapped)
        return process_expression_value(value, self.local_context)

    def evaluate_expression(self, value):
        return evaluate_expression(value, self.local_context)
