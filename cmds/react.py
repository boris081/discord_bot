import discord
from discord.ext import commands
from core.classes import Cog_Extension
from PIL import Image, ImageDraw, ImageFont
# from cmds.calculate import calculate


class React(Cog_Extension):

  @commands.command.listener()
  async def live(self, ctx):
    await ctx.send("hi")

  # 嵌入圖片生成
  @commands.command.listener()
  async def image(self, ctx, str, *args):
    img = Image.open('magic.png')

    # Fontsmsjhl
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
  @commands.command.listener()
  async def IMAGE(self, ctx, str, *args):
    img = Image.open('magic.png')

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


def setup(bot):
  bot.add_cog(React(bot))
