import discord
from discord.ext import commands
from core.classes import Cog_Extension
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import firebase.connection
import json
import random

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

db = firestore.client()
col = db.collection('bot').document("EmsUlQMGwZHtOrqjaGdR")
doc = {}

def firebaseDB():
    docs = db.collection('bot').where('count', '>' , 0).get()
    try:
        for doc in docs:
            counter = doc.to_dict()
            counter = counter['count'] + 1
            doc = {'count': counter,'name':'十十千'}
    except:
            print('read data error')
    col.update(doc)

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
    @commands.Cog.listener()
    async def on_message(self, msg):
        if len(msg.content) > 4 and '友好切磋' == msg.content[-4:]  and msg.author != self.bot.user :
            res = msg.content[:-4]
            res = res.strip()
            if random.randint(1,100) >= 99:
                if res == '十十千':
                    firebaseDB()
                await msg.channel.send(res + ' 被擊殺身亡')
            else:
                await msg.channel.send(res + ' 被擊倒了')

        if len(msg.content) > 4 and '認真對決' == msg.content[-4:]  and msg.author != self.bot.user :
            res = msg.content[:-4]
            res = res.strip()
            if random.randint(1,100) >= 90:
                if res == '十十千':
                    firebaseDB()
                await msg.channel.send(res + ' 被擊殺身亡')
            else:
                await msg.channel.send(res + ' 被擊倒了')

        if len(msg.content) > 4 and '決一死戰' == msg.content[-4:]  and msg.author != self.bot.user :
            res = msg.content[:-4]
            res = res.strip()
            if random.randint(1,100) >= 50:
                if res == '十十千':
                    firebaseDB()
                await msg.channel.send(res + ' 被擊殺身亡')
            else:
                await msg.channel.send(res + ' 被擊倒了')
        
        if len(msg.content) > 5 and '我要殺死你' == msg.content[-5:]  and msg.author != self.bot.user :
            res = msg.content[:-5]
            res = res.strip()
            if random.randint(1,100) > 85:
                await msg.channel.send(random.choice(jdata['kill_string'])%(str(msg.author.nick),random.randint(2000,10000)) + '，' + str(msg.author.nick) +' 被反殺身亡')
            else:
                if res == '十十千':
                    firebaseDB()
                await msg.channel.send(random.choice(jdata['kill_string'])%(res, random.randint(2000,10000)) + '，' + res + ' 被擊殺身亡')
        
        if '十十千死亡次數' == msg.content and msg.author != self.bot.user :
            die = db.collection('bot').where('count', '>' , 0).get()
            try:
                for doc in die:
                    counter = doc.to_dict()
                    counter = counter['count'] 
                    await msg.channel.send("十十千已被擊殺%d次"%counter)
            except:
                print('read data error')


def setup(bot):
    bot.add_cog(Event(bot))