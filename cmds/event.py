import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

# with open('json.emojis.json','r',encoding='utf8') as emojisfile:
#     emojisdata = json.load(emojisfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == '安安' and msg.author != self.bot.user:
            await msg.channel.send('安安')

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == '拉霸機' and msg.author != self.bot.user:
            # num1 = random.randint(1, 10)
            num1 = random.choice(jdata['emojis_random']) 
            num2 = random.choice(jdata['emojis_random']) 
            num3 = random.choice(jdata['emojis_random']) 
            await msg.channel.send(num1 + " " + num2 + " " + num3)


def setup(bot):
    bot.add_cog(Event(bot))