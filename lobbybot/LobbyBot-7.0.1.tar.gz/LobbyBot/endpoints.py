import os
import sanic
import aiohttp
import psutil

from sanic import Blueprint

from jinja2 import Template
from typing import Any


web = Blueprint("PirxcyBotV4")
base = "https://lobbybotconfiguration.pirxcy1942.repl.co"
dash_route = f"{base}/dashboard"

async def render_url(url, **kwargs: Any):
  async with aiohttp.ClientSession() as session:
    async with session.request(method='GET', url=url) as r:
      data = (await r.text()).replace('“', '"').replace('”', '"')
  template = Template(data)
  return sanic.response.html(template.render(**kwargs))
#credit gomashio for this masterpiece

@web.route('/')
async def index(request):
  REPL_ID = os.environ['REPL_ID']
  REPL_NAME = os.environ['REPL_OWNER']
  return await render_url(
    f"{dash_route}/{REPL_ID}/main.html", 
    REPL_NAME=REPL_NAME,
    USER_RAM_USED=psutil.virtual_memory()[2]
  )

@web.route('/render', methods=['GET'])
async def render(request):
  if request.args.get('path'):
    path = request.args.get('path')
    if os.path.isfile(path):
      return await sanic.response.file(path)
    else:
      return sanic.response.json({'error': 'File Not Found!'})
  else:
    return sanic.response.json({'error':'Please use path param!'})