import discord
from discord.ext import commands
from core.classes import Cog_Extension
import youtube_dl
import random
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)


class React(Cog_Extension):

    players = {}

    @commands.command()
    async def pic(self, ctx):
        pic = discord.File(jdata['pic'])
        await ctx.send(file=pic)

    @commands.command()
    async def 臭狗(self, ctx):
        pic = discord.File(jdata['pic2'])
        await ctx.send(file=pic)

    @commands.command()
    async def 虐狗(self, ctx):
        pic = discord.File(jdata['pic3'])
        await ctx.send(file=pic)
        
    @commands.command()
    async def 哈(self, ctx):
        pic = discord.File(jdata['pic4'])
        await ctx.send(file=pic)

    @commands.command()
    async def 老害(self, ctx):
        pic = discord.File(jdata['austonAndAlice'])
        await ctx.send(file=pic)

    @commands.command()
    async def 隨機(self, ctx):
        random_pic = random.choice(jdata['pic_random'])  
        pic = discord.File(random_pic)
        await ctx.send(file=pic)  

    # @commands.command()
    # async def GO(self, ctx):
    #     pic = discord.File(jdata['pic5'])
    #     await ctx.send(file=pic)

    @commands.command()
    async def play(self, ctx, url):
        server = ctx.message.guild
        voice_client = self.guild.voice_client(server)
        player = await voice_client.create_ytdl_play(url)
        player[server.id] = player
        player.start()

def setup(bot):
    bot.add_cog(React(bot))