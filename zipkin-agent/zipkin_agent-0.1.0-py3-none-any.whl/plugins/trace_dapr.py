#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/13 3:21 上午
# @Author  : chenxuhan  
# @File    : sw_dapr.py
# @Software: PyCharm


from opencensus.trace.execution_context import get_opencensus_tracer, get_current_span
from opencensus.trace.tracers.noop_tracer import NoopTracer


def install():
    from dapr.clients import DaprClient
    from typing import Optional, Union
    from dapr.clients.grpc.client import MetadataTuple, InvokeMethodResponse
    from google.protobuf.message import Message as GrpcMessage

    _invoke_method = DaprClient.invoke_method

    def _zk_invoke_method(
            this: DaprClient,
            app_id: str,
            method_name: str,
            data: Union[bytes, str, GrpcMessage],
            content_type: Optional[str] = None,
            metadata: Optional[MetadataTuple] = None,
            http_verb: Optional[str] = None,
            http_querystring: Optional[MetadataTuple] = None) -> InvokeMethodResponse:

        _tracer = get_opencensus_tracer()
        if not isinstance(_tracer, NoopTracer):
            if metadata is None:
                metadata = []
            metadata.extend([(key, val) for key, val in _tracer.propagator.to_headers(_tracer.span_context).items()])
        res = _invoke_method(this, app_id, method_name, data, content_type, metadata, http_verb, http_querystring)

        return res

    DaprClient.invoke_method = _zk_invoke_method
