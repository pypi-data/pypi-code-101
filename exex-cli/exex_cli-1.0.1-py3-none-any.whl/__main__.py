from .application import application
from .commands import ExtractCommand

if __name__ == "__main__":
    extract = ExtractCommand()
    application.add(extract.default())
    application.run()
