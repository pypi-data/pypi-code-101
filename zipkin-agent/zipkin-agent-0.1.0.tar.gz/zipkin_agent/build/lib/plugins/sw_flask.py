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

from zipkin_agent import Layer, Component, config
from zipkin_agent.agent import init_zk_tracer
from zipkin_agent.trace import tags

from opencensus.trace.propagation.trace_context_http_header_format import TraceContextPropagator
from opencensus.trace.status import Status
from opencensus.trace.execution_context import get_opencensus_tracer, get_current_span


def install():
    from flask import Flask
    _full_dispatch_request = Flask.full_dispatch_request
    _handle_user_exception = Flask.handle_user_exception
    _handle_exception = Flask.handle_exception

    def params_tostring(params):
        return "\n".join([k + '=[' + ",".join(params.getlist(k)) + ']' for k, _ in params.items()])

    def _zk_full_dispatch_request(this: Flask):
        import flask
        req = flask.request

        if 'traceparent' in req.headers:
            init_zk_tracer(span_context=TraceContextPropagator().from_headers(req.headers))
            resp = _full_dispatch_request(this)
            return resp
        else:
            init_zk_tracer()
            with get_opencensus_tracer().span(name=req.url.split("?")[0]) as span:
                span.add_attribute('kind', 'service')
                span.add_attribute('layer', Layer.Http.name)
                span.add_attribute('component', Component.Flask.name)
                span.add_attribute('peer', '%s:%s' % (req.environ["REMOTE_ADDR"], req.environ["REMOTE_PORT"]))
                span.add_attribute(tags.HttpMethod, req.method)
                span.add_attribute(tags.HttpUrl, req.url.split("?")[0])
                span.add_attribute(tags.HttpParams, params_tostring(req.values)[0:config.http_params_length_threshold])
                resp = _full_dispatch_request(this)
                span.set_status(Status(code=resp.status_code))
                span.add_attribute(tags.HttpStatus, resp.status_code)
                return resp

    def _zk_handle_user_exception(this: Flask, e):
        if e is not None:
            entry_span = get_current_span()
            if entry_span is not None:
                entry_span.set_status(Status.from_exception(e))

        return _handle_user_exception(this, e)

    def _zk_handle_exception(this: Flask, e):
        if e is not None:
            entry_span = get_current_span()
            if entry_span is not None:
                entry_span.set_status(Status.from_exception(e))

        return _handle_exception(this, e)


    Flask.full_dispatch_request = _zk_full_dispatch_request
    Flask.handle_user_exception = _zk_handle_user_exception
    Flask.handle_exception = _zk_handle_exception