from . import routes

@routes.app_errorhandler(404)
def e404(error):
    return {'status': 404}, 404