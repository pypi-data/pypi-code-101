from tortoise import Tortoise
from pydantic import BaseModel, Field, AnyUrl

from .base import BaseCog


class OrmCogConfig(BaseModel):
    database_uri: AnyUrl = Field("sqlite://{sqlite_path}")


class OrmCog(BaseCog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.database_path: str = kwargs.get("database_path")
        self.models_module: str = kwargs.pop("models_module")

    async def on_bot_close(self):
        await Tortoise.close_connections()

    async def on_startup(self):
        await Tortoise.init(
            db_url=self.bot.config.orm.database_uri.format(
                sqlite_path=self.database_path
            ),
            modules={"models": [self.models_module]},
        )

        await Tortoise.generate_schemas(safe=True)
