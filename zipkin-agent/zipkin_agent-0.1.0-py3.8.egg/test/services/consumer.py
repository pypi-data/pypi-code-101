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

import requests
import os
#
# from zipkin_agent import agent, config
#
#
# config.logging_level = 'DEBUG'
# config.flask_collect_http_params = True
# agent.start()

from flask import Flask

app = Flask(__name__)


@app.route("/echo", methods=["POST", "GET"])
def user_hander():
    return 'OK'


@app.route("/users", methods=["POST", "GET"])
def application():
    with requests.get('http://localhost:3523/v1.0/invoke/node_c/method/echo') as resp:
        return resp.text


@app.route("/test", methods=["POST", "GET"])
def test():
    with requests.get('http://localhost:3523/v1.0/invoke/node_c/method/echo') as resp:
        print(resp.text)

    with requests.get('http://localhost:3522/v1.0/invoke/node_b/method/users') as resp:
        return resp.text


if __name__ == '__main__':
    if os.getenv('SW_AGENT_NAME') == 'node_c':
        PORT = 1233
    elif os.getenv('SW_AGENT_NAME') == 'node_b':
        PORT = 1232
    elif os.getenv('SW_AGENT_NAME') == 'node_a':
        PORT = 1231
    app.run(host='0.0.0.0', port=PORT, debug=True)
