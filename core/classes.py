from discord.ext import commands
from db.DBHepler import DBHepler

class Cog_Extension(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
      self.DBHepler = DBHepler
