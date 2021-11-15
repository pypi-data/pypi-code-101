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


from zipkin_agent import config, plugins, loggings
from opencensus.trace.tracer import Tracer
from opencensus.ext.zipkin.trace_exporter import ZipkinExporter
from opencensus.trace.samplers import AlwaysOnSampler
from opencensus.trace.execution_context import set_opencensus_tracer


__started = False


def __init():
    ze = ZipkinExporter(
        service_name=config.service_name,
        host_name=config.zipkin_host,
        port=config.zipkin_port,
        endpoint='/api/v2/spans')
    setattr(config, 'zipkin_reporter', ze)

    plugins.install()


def start():
    global __started
    if __started:
        return
    __started = True

    loggings.init()

    __init()


def started():
    return __started


def init_zk_tracer(**kwargs):
    _tracer = Tracer(
        exporter=getattr(config, 'zipkin_reporter'),
        sampler=AlwaysOnSampler(),
        **kwargs
    )
    set_opencensus_tracer(_tracer)