import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='>')

class Event(Cog_Extension):
    # @commands.Cog.listener()
    # async def on_message(self, msg):
    #     if msg.content == '安安' and msg.author != self.bot.user:
    #         await msg.channel.send('安安')

    # @commands.Cog.listener()
    # async def on_message(self, msg):
    #     if msg.content == '拉霸機' and msg.author != self.bot.user:
    #         # num1 = random.randint(1, 10)
    #         num1 = random.choice(jdata['emojis_random'])
    #         num2 = random.choice(jdata['emojis_random'])
    #         num3 = random.choice(jdata['emojis_random'])
    #         await msg.channel.send(num1 + " " + num2 + " " + num3)

    # @commands.Cog.listener()
    # async def on_message(self, msg):

    # @commands.Cog.listener()
    # async def on_message_delete(self, msg):
        # channel = bot.get_channel(781920817088036904)        
        # await msg.send("訊息刪除: " + str(msg.author) + " : " + str(msg.content))


def setup(bot):
    bot.add_cog(Event(bot))
