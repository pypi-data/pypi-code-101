from mimetypes import guess_type
from pathlib import Path

import netron
from tensorboard.backend import http_util
from tensorboard.plugins.base_plugin import TBPlugin, FrontendMetadata
from werkzeug.wrappers import Request


class Netron(TBPlugin):
    plugin_name = 'netron'

    def __init__(self, context):
        super().__init__(context)
        self._static_path = Path(netron.__file__).parent
        self._base_path = Path(f'/data/plugin/{self.plugin_name}/static')

    def frontend_metadata(self):
        return FrontendMetadata(
            tab_name='Netron',
            es_module_path='/render.js',
            disable_reload=True
        )

    def get_plugin_apps(self):
        return {
            '/render.js': self._serve_render,
            '/static/*': self._serve_static
        }

    def is_active(self):
        return False

    @Request.application
    def _serve_render(self, request):
        return http_util.Respond(
            request=request,
            content='export const render = () => window.location = "./static/index.html"',
            content_type='text/javascript'
        )

    @Request.application
    def _serve_static(self, request):
        rel_path = Path(request.path).relative_to(self._base_path)
        abs_path = self._static_path.joinpath(rel_path)
        if abs_path.is_file():
            with open(abs_path, 'r') as file:
                content = file.read()
            return http_util.Respond(request, content, guess_type(abs_path)[0])
        else:
            return http_util.Respond(request, 'NotFound', 'text/plain', 404)
