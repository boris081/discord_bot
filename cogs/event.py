from discord.ext import commands
from discord.ext.commands import Context


# Here we name the cog and create a new class for the cog.
class Event(commands.Cog, name="event"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(nema="破麻", description="7414")
    async def 破麻(self, context: Context) -> None:
        await context.send('https://media.discordapp.net/attachments/662554422471294997/1156636646377267310/image.png?ex=65f1dbd1&is=65df66d1&hm=f7599f3aa66d6e726426694c3e13ab47f141971da5271f81e292ea79ff444b15')

# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot) -> None:
    await bot.add_cog(Event(bot))
