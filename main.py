## update 2024/11/02
# optimize on_message_delete function
# import keep_alive
import discord
from discord.ext import commands
import os
import json
import io 
import aiohttp
import requests
import datetime
from PIL import Image, ImageDraw, ImageFont

tzone = datetime.timezone(datetime.timedelta(hours=8))
current_time = datetime.datetime.now(tz=tzone)

with open('json/key.json', 'r', encoding='utf8') as jfile:
  jdata = json.load(jfile)
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='>', intents=intents)


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
  s = f"From \"{message.guild.name} -> {message.channel}\"\n"
  s += f"User \"{message.author.global_name}({message.author})\" delete a message:\n"
  if message.attachments:
    body = f"{message.attachments[0].url}\n"
    embed = discord.Embed(title=s, description=body, timestamp=current_time, colour=discord.Colour.dark_orange())
    await channel.send(embed=embed)
  else:
    body = f"{message.content}\n"
    embed = discord.Embed(title=s, description=body, timestamp=current_time, colour=discord.Colour.dark_orange())
    await channel.send(embed=embed)

@bot.event
async def on_message(message):
  channel = bot.get_channel(1304407628549586995)  #圖片監視器
  s = f"From \"{message.guild.name} -> {message.channel}\"\n"
  s += f"User \"{message.author.global_name}({message.author})\" sned a image:\n"

  if message.attachments and message.author!=bot.user:
    response = requests.get(message.attachments[0].url)
    image_data = io.BytesIO(response.content)
    file = discord.File(image_data, filename='image.png')
    embed = discord.Embed(title=s, timestamp=current_time, colour=discord.Colour.dark_orange()) 
    embed.set_image(url="attachment://image.png")
    await channel.send(embed=embed, file=file)

# cooldown error-handling
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await print("on_command_error")


@bot.command()
async def hi(ctx):
  await ctx.send('hello')  # 发送 'hello' 消息给用户


@bot.command()
async def 破麻(ctx):
  await ctx.send(
    'https://media.discordapp.net/attachments/662554422471294997/1156636646377267310/image.png?ex=65f1dbd1&is=65df66d1&hm=f7599f3aa66d6e726426694c3e13ab47f141971da5271f81e292ea79ff444b15'
  )


# 嵌入圖片生成
@bot.command()
async def image(ctx, str, *args):
  img = Image.open('magic.png')
  font = ImageFont.truetype('msjhbd.ttc', 48)
  draw = ImageDraw.Draw(img)
  for val in args:
    str = str + val
  print("str ", str.replace("_", " "))
  if (',' in str):
    text1, text2 = str.split(',', 1)
  else:
    text1 = str
    text2 = ''

  x1 = 455
  y1 = 400
  draw.text((x1, y1), text1.replace("_", " "), font=font, fill=(0, 0, 0))

  x1 = 455
  y1 = 450
  draw.text((x1, y1), text2.replace("_", " "), font=font, fill=(0, 0, 0))
  width, height = img.size
  img.save('re_magic.png')
  await ctx.send(file=discord.File('re_magic.png'))


# 嵌入圖片生成
@bot.command()
async def IMAGE(ctx, str, *args):
  img = Image.open('magic.png')
  print(str)
  # Fontsmsjhl
  font = ImageFont.truetype('msjhbd.ttc', 48)
  draw = ImageDraw.Draw(img)
  for val in args:
    str = str + val
  print("str ", str)
  if (',' in str):
    text1, text2 = str.split(',', 1)
  else:
    text1 = str
    text2 = ''

  x1 = 455
  y1 = 400
  draw.text((x1, y1), text1.replace("_", " "), font=font, fill=(0, 0, 0))

  x1 = 455
  y1 = 450
  draw.text((x1, y1), text2.replace("_", " "), font=font, fill=(0, 0, 0))
  width, height = img.size
  img.save('re_magic.png')
  await ctx.send(file=discord.File('re_magic.png'))


# 搜索有cmds底下文件
for filename in os.listdir('./cmds'):
  if filename.endswith('.py'):  # 判斷結尾是否為.py
    bot.load_extension(F'cmds.{filename[:-3]}')

if __name__ == "__main__":
  # keep_alive.keep_alive()
  bot.run(jdata['TOKEN'])
