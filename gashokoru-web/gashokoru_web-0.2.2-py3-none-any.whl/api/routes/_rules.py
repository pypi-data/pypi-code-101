from . import routes

from .admin import *
from .user import *


# #############
#  USER ALIASES
# #############

routes.add_url_rule("/generate/id:<int:id>", "generate", generate)
routes.add_url_rule("/generer/id:<int:id>", "generate", generate)
routes.add_url_rule("/gen/id:<int:id>", "generate", generate)
routes.add_url_rule("/new/id:<int:id>", "generate", generate)

routes.add_url_rule(    
                        "/out/generate", "out_generate", out_generate, 
                        methods=['POST']
                    )

# #############
# ADMIN ALIASES
# #############

routes.add_url_rule("/", "index", index)
