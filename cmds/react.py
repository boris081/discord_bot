import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random
from db.DBHepler import DBHepler
from config import ConfigDefaults
from PIL import Image, ImageDraw, ImageFont
# from cmds.calculate import calculate

with open(ConfigDefaults.setting_file, 'r', encoding='utf8') as jfile:
    jsetting = json.load(jfile)


class React(Cog_Extension):
    # @commands.command()
    # async def read(self, ctx):
    #   with DBHepler(ConfigDefaults.db_path) as db:
    #       user_point = db.get('GAME', '*')
    #       print(user_point)

    # @commands.command()
    # async def 賭場(self, ctx, id):
    #   await ctx.send("")

  
    @commands.command()
    async def 斗內(self, ctx, target_id, point: int):
        with DBHepler(ConfigDefaults.db_path) as db:
            user_id = int(ctx.author.id)
            target_id = target_id[3:-1]

            user_point = db.select_point_by_id(user_id)  #user point
            target_point = db.select_point_by_id(target_id)  #目標point

            # if (ctx.author.id == 315483283964166155):
            #   await ctx.send(target_id + "增加{0}賭金".format(point))
            #   db.update_point_by_id(target_id, target_point+point)
            #   return

            if (user_point < point or point <= 0):
                await ctx.send("孝子沒錢還斗")
                return

            await ctx.send("<@" + target_id + ">" + "增加{0}賭金".format(point))
            db.update_point_by_id(user_id, user_point - point)
            db.update_point_by_id(target_id, target_point + point)

    # 嵌入圖片生成
    @commands.command()
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
    @commands.command()
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

    @commands.command()
    async def map(self, ctx, map_id: str, route: str):
        with open('map.json', 'r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        try:
            for item in jdata[map_id]:
                await ctx.send(item[route])
        except IOError:
            pass

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def 拉霸機(self, ctx, point: str):
        with DBHepler(ConfigDefaults.db_path) as db:
            user_id = int(ctx.author.id)
            user_point = db.select_point_by_id(user_id)
            if (point == 'ALL' or point == 'all'):
                point = int(user_point)
            else:
                point = int(point)

            if (user_point < point or point < 0):
                await ctx.send("沒錢就不要賭，下面一位")
                return
            num1 = random.choice(jsetting['emojis_random'])
            num2 = random.choice(jsetting['emojis_random'])
            num3 = random.choice(jsetting['emojis_random'])

            if (num1 == num2 == num3):
                winpoint = point * 30
                user_point = user_point + winpoint

                await ctx.send(
                    '{num1}{num2}{num3} 恭喜你得到{winpoint} 剩餘{user_point}'.format(
                        num1=num1,
                        num2=num2,
                        num3=num3,
                        winpoint=winpoint,
                        user_point=user_point))
            else:
                user_point = user_point - point
                await ctx.send(
                    '{num1}{num2}{num3}輸掉了{point}你還有{user_point}'.format(
                        num1=num1,
                        num2=num2,
                        num3=num3,
                        point=point,
                        user_point=user_point))
            db.update_point_by_id(user_id, user_point)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def 大小(self, ctx, s: str, point: str):
        num = random.choice(jsetting['roll'])
        with DBHepler(ConfigDefaults.db_path) as db:
            user_id = int(ctx.author.id)
            user_point = db.select_point_by_id(user_id)

            if (point == 'ALL' or point == 'all'):
                point = int(user_point)
            else:
                point = int(point)

            if (user_point < point or point < 0):
                await ctx.send("沒錢就不要賭，下面一位")
                return

            if (s == num):
                user_point = user_point + point * 2
            else:
                user_point = user_point - point

            await ctx.send("結果為{} 剩餘{}".format(num, user_point))
            db.update_point_by_id(user_id, user_point)

    @commands.command()
    async def 刮刮樂(self, ctx):
        r = random.randrange(1, 10)
        s1 = "神運刮刮樂帶給你神運"
        s2 = "無料空刮"
        if (r == 1): await ctx.send(s1)
        else: await ctx.send(s2)

    @commands.command()
    async def 賭金(self, ctx):
        with DBHepler(ConfigDefaults.db_path) as db:
            user_point = db.select_point_by_id(ctx.author.id)
            await ctx.send(str(ctx.author.nick) + '擁有' + str(user_point))

    @commands.command()
    async def 排行(self, ctx):
        with DBHepler(ConfigDefaults.db_path) as db:
            user_point = db.get('GAME Order by point DESC', 'username,point')
            limit = 10
            dlist = []
            for i, j in user_point:
                member = str(i) + ':' + str(j)
                dlist.append(member)
                if (len(dlist) > limit):
                    break
            await ctx.send('\n'.join(dlist))


def setup(bot):
    bot.add_cog(React(bot))
