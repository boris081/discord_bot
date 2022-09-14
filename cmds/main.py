from discord.ext import commands
from core.classes import Cog_Extension


class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        print("hi")


def setup(bot):
    bot.add_cog(Main(bot))
