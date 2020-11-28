import discord
from discord.ext import commands
from core.classes import Cog_Extension
import os
import json

intents = discord.Intents.default()

with open('key.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='>', description="This is a Helper Bot")


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message_delete():
    channel = bot.get_channel(781920817088036904)        
    await channel.send("訊息刪除: " + str(msg.author) + " : " + str(msg.content))

# 搜索有cmds底下文件
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):  # 判斷結尾是否為.py
        bot.load_extension(F'cmds.{filename[:-3]}')


if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
