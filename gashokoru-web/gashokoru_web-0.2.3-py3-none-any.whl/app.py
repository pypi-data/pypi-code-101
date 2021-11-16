from .config import config
from .api import app
from confuse import ConfigTypeError, NotFoundError

# STARTING FLASK APP
#####################
def main():

    try:
        app.run(
                host=config['ingress']['host'].get(str),
                port=config['ingress']['port'].get(int)
            )
    except ConfigTypeError:
        print("Wrong type for host (should be str) and/or port (should be positive int) in configuration file")
    except NotFoundError:
        print("Ingress host and/or port not found in configuration file")
    except:
        print("Could not start Flask application")
