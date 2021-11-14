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

class Embed:
    def __init__(self, title: str, description: str = "", color: str = "#5865F2"):
        self.title = title
        self.description = description
        self.color = color
        self.json = {"title": title, "description": description, "color": int(color.replace("#", "0x"), 16), "fields": []}

    def set_url(self, url: str):
        self.url = url
        self.json["url"] = url
    
    def set_timestamp(self, timestamp: str):
        self.timestamp = timestamp
        self.json["timestamp"] = timestamp

    def set_footer(self, text: str, icon_url: str = ""):
        self.footer = {"text": text, "icon_url": icon_url}
        self.json["footer"] = {"text": text, "icon_url": icon_url}

    def set_image(self, url: str):
        self.image = {"url": url}
        self.json["image"] = {"url": url}

    def set_thumbnail(self, url: str):
        self.thumbnail = {"url": url}
        self.json["thumbnail"] = {"url": url}

    def set_video(self, url: str, width: int, height: int):
        self.video = {"url": url, "height": height, "width": width}
        self.json["video"] = {"url": url, "height": height, "width": width}

    def set_provider(self, name: str, url: str = ""):
        self.provider = {"name": name, "url": url}
        self.json["provider"] = {"name": name, "url": url}
    
    def set_author(self, name: str, url: str = "", icon_url: str = ""):
        self.author = {"name": name, "url": url, "icon_url": icon_url}
        self.json["author"] = {"name": name, "url": url, "icon_url": icon_url}
    
    def add_field(self, name: str, value: str = " ", inline: bool = True):
        self.json["fields"].append({"name": name, "value": value, "inline": inline})

    def keys(self):
        return self.json.keys()

    def __getitem__(self, item):
        return self.json[item]
