from mod3rd.admin_windup.secsys import router as secsys_router

from mod3rd.admin_windup.editor import static_files
from mod3rd.admin_windup.file_api import router
from mod3rd.admin_windup.content import router as content_router

from modext.auto_config.ext_spec import Plugin


class WindupAdminUtils(Plugin):
    def __init__(self):
        super().__init__()
        self.caption = "WindUp Admin Utils"
        self.path_spec = "mod3rd.admin_windup"
        self.generators = [secsys_router, static_files, router, content_router]
        self.url_caption_tuple_list = [
            (secsys_router.root + "/secsys", None),
            (static_files.root + "/#", None),
            (router.root + "/browse", None),
            (content_router.root + "/generators", None),
        ]


# deprecated
class FileUtils(WindupAdminUtils):
    pass


app_ext = WindupAdminUtils()
