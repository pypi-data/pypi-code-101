from cleo import Application as CleoApplication

from exex_cli.application_config import ApplicationConfig

custom_config = ApplicationConfig(name="exex-cli", version="1.0.2")
application = CleoApplication(config=custom_config)
