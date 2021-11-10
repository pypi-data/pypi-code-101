import discord
from discord.ext import commands, tasks

class easyCode:
  def __init__(self, prefix="!", token):
    self.bot = commands.Bot(intents=discord.Intents.all(), command_prefix=prefix)
    self.token = token
    