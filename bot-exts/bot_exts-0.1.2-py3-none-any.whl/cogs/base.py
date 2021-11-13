from nextcord.ext import commands


class BaseCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.bot.loop.create_task(self.on_startup())

    async def on_bot_close(self):
        pass

    async def on_startup(self):
        pass
