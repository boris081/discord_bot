import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

bot.run("NjQzMDQwMjg4NjIwNjc1MDcy.XcftBA.sa5WQHF7lhg6poSdgE0L0aPzaW8")
