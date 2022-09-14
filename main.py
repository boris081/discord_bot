import keep_alive
from discord.ext import commands
import os
import json
from dislash import InteractionClient, ContextMenuInteraction

with open('json/key.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='>', description="This is a Helper Bot")


@bot.event
async def on_ready():
    # channel = bot.get_channel(782312791615733790)  #艦娘許願池頻道
    channel = bot.get_channel(662554422471294997)  #艦娘閒聊頻道
    # channel = bot.get_channel(781920817088036904) #私人ㄐㄐ人頻道
    # for i in range(5):
    # await channel.send("我是第四個妓安")
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message_delete(message):
    channel = bot.get_channel(821324099791093770)  #監視器
    # channel = bot.get_channel(782312791615733790) 艦娘許願池頻道
    # 662554422471294997 閒聊
    s = "從<" + str(message.channel) + ">的訊息刪除: " + str(message.author)
    if message.attachments:
        s = s + " : " + message.attachments[0].url
        await channel.send(s)
        print(s)
    else:
        s = s + " : " + str(message.content)
        print(s)
        await channel.send(s)


# cooldown error-handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await print("on_command_error")


# #  APPS
inter_client = InteractionClient(
    bot, test_guilds=[662554260969619468, 683651851711021198])


@inter_client.user_command(name="Apex")
async def apex(ctx: ContextMenuInteraction):
    # User commands always have only this ^ argument
    # print(ctx.member.id)
    str = "<@{}> it's apex time".format(ctx.member.id)
    await ctx.respond(str)


# 搜索有cmds底下文件
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):  # 判斷結尾是否為.py
        bot.load_extension(F'cmds.{filename[:-3]}')

if __name__ == "__main__":
    keep_alive.keep_alive()
    bot.run(jdata['TOKEN'])
