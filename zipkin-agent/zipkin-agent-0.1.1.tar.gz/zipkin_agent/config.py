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
import os
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List

QUEUE_TIMEOUT = 1  # type: int

RE_IGNORE_PATH = re.compile('^$')  # type: re.Pattern

options = None  # here to include 'options' in globals
options = globals().copy()  # THIS MUST PRECEDE DIRECTLY BEFORE LIST OF CONFIG OPTIONS!

service_name = os.getenv('AGENT_NAME') or 'Python Service Name'  # type: str
zipkin_host = os.getenv('ZIPKIN_HOST') or 'localhost'
zipkin_port = os.getenv('ZIPKIN_PORT') or 9411
force_tls = os.getenv('AGENT_FORCE_TLS', '').lower() == 'true'  # type: bool
protocol = (os.getenv('AGENT_PROTOCOL') or 'grpc').lower()  # type: str
authentication = os.getenv('AGENT_AUTHENTICATION')  # type: str
logging_level = os.getenv('AGENT_LOGGING_LEVEL') or 'INFO'  # type: str
disable_plugins = (os.getenv('AGENT_DISABLE_PLUGINS') or '').split(',')  # type: List[str]
max_buffer_size = int(os.getenv('AGENT_MAX_BUFFER_SIZE', '1000'))  # type: int
ignore_suffix = os.getenv('IGNORE_SUFFIX') or '.jpg,.jpeg,.js,.css,.png,.bmp,.gif,.ico,.mp3,' \
                                                 '.mp4,.html,.svg '  # type: str
flask_collect_http_params = True if os.getenv('FLASK_COLLECT_HTTP_PARAMS') and \
                                    os.getenv('FLASK_COLLECT_HTTP_PARAMS') == 'True' else False  # type: bool
http_params_length_threshold = int(os.getenv('HTTP_PARAMS_LENGTH_THRESHOLD') or '1024')  # type: int
trace_ignore_path = os.getenv('TRACE_IGNORE_PATH') or ''  # type: str
profile_active = True if os.getenv('AGENT_PROFILE_ACTIVE') and \
                         os.getenv('AGENT_PROFILE_ACTIVE') == 'True' else False  # type: bool
profile_task_query_interval = int(os.getenv('PROFILE_TASK_QUERY_INTERVAL') or '20')

options = {key for key in globals() if key not in options}  # THIS MUST FOLLOW DIRECTLY AFTER LIST OF CONFIG OPTIONS!


def init(**kwargs):
    glob = globals()

    for key, val in kwargs.items():
        if key not in options:
            raise KeyError('invalid config option %s' % key)

        glob[key] = val
