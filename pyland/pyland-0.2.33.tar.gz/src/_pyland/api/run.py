# run.py
from .main import app as application


def run_server(host="0.0.0.0", port=5000, debug=True, use_reloader=True):
    application.run(port=port, host=host, use_reloader=use_reloader, debug=debug)


if __name__ == "__main__":
    application.run(port=5000, host="0.0.0.0", use_reloader=True, debug=True)
