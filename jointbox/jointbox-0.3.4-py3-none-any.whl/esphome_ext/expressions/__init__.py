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

from typing import Optional

import jinja2
from jinja2.environment import Environment

from ..expressions import filters as custom_filters

__ENVIRONMENT__: Environment = None  # type: ignore

FILTER_FUNCTION_PREFIX = "filter_"


class TemplateRenderingError(Exception):
    def __init__(self, msg: str, original_error: Exception) -> None:
        msg += ": " + str(original_error)
        super().__init__(msg)
        self.original_error = original_error


def _get_jinja2_env() -> Environment:
    global __ENVIRONMENT__
    if __ENVIRONMENT__ is None:
        __ENVIRONMENT__ = Environment()
        # Configuring filters
        for filter_fn_name in dir(custom_filters):
            if filter_fn_name.startswith(FILTER_FUNCTION_PREFIX):
                filter_name = filter_fn_name.replace(FILTER_FUNCTION_PREFIX, "", 1)
                filter_fn = getattr(custom_filters, filter_fn_name)
                if callable(filter_fn):
                    __ENVIRONMENT__.filters[filter_name] = getattr(custom_filters, filter_fn_name)
    return __ENVIRONMENT__


def contains_expression(value) -> bool:
    return "{{" in value or "{%" in value


def is_single_expression_str(value) -> bool:
    if isinstance(value, str):
        normalized_value = value.strip()
        env = _get_jinja2_env()
        if normalized_value.startswith(env.variable_start_string) and normalized_value.endswith(
            env.variable_end_string
        ):
            normalized_value = normalized_value[len(env.variable_start_string) : -1 * len(env.variable_end_string)]
            return not contains_expression(normalized_value)
    return False


def unwrap_expression(value: str) -> Optional[str]:
    if is_single_expression_str(value):
        env = _get_jinja2_env()
        return value.strip()[len(env.variable_start_string) : -1 * len(env.variable_end_string)]
    return None


def _create_template_for_str(str_val: str) -> jinja2.Template:
    # Configure template instance with required filters, extensions, blocks here
    return _get_jinja2_env().from_string(str_val, template_class=jinja2.Template)


def register_global(name: str, val):
    _get_jinja2_env().globals[name] = val


def register_globals(dict_: dict):
    env = _get_jinja2_env()
    for k, v in dict_.items():
        env.globals[k] = v


def process_expression_value(value, context: dict):
    if not isinstance(value, str):
        return value  # Skip non-string values
    if not contains_expression(value):
        return value  # If there are no Jinja2 tags - just skip it too
    try:
        template = _create_template_for_str(value)
        return template.render(context)
    except jinja2.TemplateError as e:
        raise TemplateRenderingError('Error in expression value "{}"'.format(value), e) from e


def evaluate_expression(expression: str, context: dict):
    try:
        compiled = _get_jinja2_env().compile_expression(expression)
        return compiled(context)
    except jinja2.TemplateError as e:
        raise TemplateRenderingError('Error in expression value "{}"'.format(expression), e) from e
