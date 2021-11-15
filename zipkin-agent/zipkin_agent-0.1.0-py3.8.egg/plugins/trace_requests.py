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


from opencensus.trace.execution_context import get_opencensus_tracer
from opencensus.trace.tracers.noop_tracer import NoopTracer


def install():
    from requests import Session

    _request = Session.request

    def _zk_request(this: Session, method, url,
                    params=None, data=None, headers=None, cookies=None, files=None,
                    auth=None, timeout=None, allow_redirects=True, proxies=None,
                    hooks=None, stream=None, verify=None, cert=None, json=None):

        from urllib.parse import urlparse
        url_param = urlparse(url)

        _tracer = get_opencensus_tracer()

        # ignore trace reporter self request
        if isinstance(_tracer, NoopTracer) or _tracer.exporter.get_url.endswith(url_param.netloc + url_param.path):
            return _request(this, method, url, params, data, headers, cookies, files, auth, timeout,
                            allow_redirects,
                            proxies,
                            hooks, stream, verify, cert, json)

        if not isinstance(_tracer, NoopTracer):
            if headers is None:
                headers = {}
            trace_headers = _tracer.propagator.to_headers(_tracer.span_context)
            for key in trace_headers:
                headers[key] = trace_headers[key]
        res = _request(this, method, url, params, data, headers, cookies, files, auth, timeout,
                       allow_redirects,
                       proxies,
                       hooks, stream, verify, cert, json)

        return res

    Session.request = _zk_request
