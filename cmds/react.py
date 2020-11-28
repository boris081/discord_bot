import discord
from discord.ext import commands
from core.classes import Cog_Extension


class React(Cog_Extension):
    @commands.command()
    async def sum(self, ctx, numOne: int, numTwo: int):
        await ctx.send(numOne + numTwo)

    @commands.command()
    async def map(self, ctx, string: str):
        await ctx.send(string)

    @commands.command()
    async def channel(self, ctx, string: str):
        print(ctx.get_channels())
        await ctx.send(string)

    # @commands.command()
    # async def 晚安(self, ctx):
    #     await ctx.send(str(client.users.) + '晚安')


def setup(bot):
    bot.add_cog(React(bot))
