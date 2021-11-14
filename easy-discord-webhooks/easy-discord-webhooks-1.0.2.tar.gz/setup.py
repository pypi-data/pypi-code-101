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

from distutils.core import setup

setup(
  name = 'easy-discord-webhooks',
  packages = ['easy_discord_webhooks'],
  version = '1.0.2',
  license='MIT',
  description = 'An easy and simplistic way to execute and modify a Discord webhook all from Python.',
  long_description_content_type="text/markdown",
  long_description=open('README.rst').read(),
  author = 'Ben Tettmar',
  author_email = 'hello@benny.fun',
  url = 'https://github.com/bentettmar/easy-discord-webhooks',
  download_url = 'https://github.com/bentettmar/easy-discord-webhooks/archive/refs/tags/1.0.0.tar.gz',
  keywords = ['discord', 'webhook', 'easy', "discord webhook", "webhook discord", "easy discord webhook", "discord webhook easy"],
  install_requires=["requests"]
)