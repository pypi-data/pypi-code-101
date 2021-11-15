#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from functools import wraps
import inspect

from zipkin_agent import Layer, Component
from opencensus.trace.execution_context import get_opencensus_tracer


def trace(
        op: str = None,
        layer: Layer = Layer.Unknown,
        component: Component = Component.Unknown,
        tags: dict = None,
):
    def decorator(func):
        _op = op or func.__name__

        if inspect.iscoroutinefunction(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                _tracer = get_opencensus_tracer()
                span = _tracer.span(name=_op)
                span.add_attribute('layer', layer.name)
                span.add_attribute('component', component.name)
                if tags:
                    for tag_k, tag_v in tags.items():
                        span.add_attribute(tag_k, tag_v)
                with span:
                    return await func(*args, **kwargs)
            return wrapper

        else:
            @wraps(func)
            def wrapper(*args, **kwargs):
                _tracer = get_opencensus_tracer()
                span = _tracer.span(name=_op)
                span.add_attribute('layer', layer.name)
                span.add_attribute('component', component.name)
                if tags:
                    for tag_k, tag_v in tags.items():
                        span.add_attribute(tag_k, tag_v)
                with span:
                    return func(*args, **kwargs)
            return wrapper

    return decorator


def runnable(
        op: str = None,
        layer: Layer = Layer.Unknown,
        component: Component = Component.Unknown,
        tags: dict = None,
):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            _op = op or "Thread/"+func.__name__
            _tracer = get_opencensus_tracer()
            with _tracer.new_local_span(name=_op) as span:
                span.add_attribute('layer', layer.name)
                span.add_attribute('component', component.name)
                if tags:
                    for tag_k, tag_v in tags.items():
                        span.add_attribute(tag_k, tag_v)
                func(*args, **kwargs)

        return wrapper

    return decorator
