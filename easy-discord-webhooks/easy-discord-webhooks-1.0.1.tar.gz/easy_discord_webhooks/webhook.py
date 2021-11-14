# MIT License

# Copyright (c) 2021 Ben Tettmar

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json
import requests

class Webhook:
    def __init__(self, url):
        response = requests.get(url).json()
        self.type = response["type"]
        self.id = response["id"]
        self.name = response["name"]
        self.avatar = response["avatar"]
        self.channelId = response["channel_id"]
        self.guildId = response["guild_id"]
        self.applicationId = response["application_id"]
        self.token = response["token"]

    def __str__(self):
        return self.name

    def edit(self, name=""):
        url = f"https://discord.com/api/webhooks/{self.id}/{self.token}"
        response = requests.patch(url, headers={"Content-Type": "application/json"}, data=json.dumps({"name": name}))
        self.name = response.json()["name"]

    def delete(self):
        requests.delete(f"https://discord.com/api/webhooks/{self.id}/{self.token}")

    def send(self, message="", embed={}):
        url = f"https://discord.com/api/webhooks/{self.id}/{self.token}"
        if embed == {}:
            requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps({"content": message}))
        else:
            requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps({"content": message, "embeds": [dict(embed)]}))