from discord.ext import commands
from core.classes import Cog_Extension
from db.DBHepler import DBHepler
from config import ConfigDefaults


class Event(Cog_Extension):
    solit = 0
    @commands.Cog.listener()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def on_message(self, msg):
      if(msg.channel=="854340688199286824"):
        print(msg.author.id)
      # with DBHepler(ConfigDefaults.db_path) as db:
      #   user_id = msg.author.id
      #   user_point = db.select_point_by_id(user_id)     
      #   # 新成員寫入資料庫
      #   if user_point=="None":
      #     ls = []
      #     data = (user_id, str(msg.author.nick), int(msg.guild.id), 1000)
      #     for i in data:
      #       ls.append(i)
      #     db.insert_new(data)
        # else:
        #   user_point = int(user_point) + 20
          # db.update_point_by_id(int(user_id), int(user_point))

      # global solitr
      # solitr_str = ['天', '子', '大', 'ㄐ', 'ㄐ']
      # if(msg.content not in solitr_str and solitr != 0):
      #   solitr = 0
      # if(msg.content == '天'):
      #   solitr = 1
      #   print('天')
      # if(msg.content == '子' and solitr==1):
      #   solitr = 2
      #   print('子')
      # if(msg.content == '大' and solitr==2):
      #   solitr = 3
      #   print('大')
      # if(msg.content == 'ㄐ' and solitr==3):
      #   solitr = 4
      #   print('ㄐ')
      # elif(msg.content == 'ㄐ' and solitr==4):
      #   solitr = 0
      #   channel = msg.channel
      #   await channel.send('https://media.discordapp.net/attachments/841352984340332574/894215200272678942/d8299814a67b0da90d4df3de960f92a2.gif')
      #   print('接龍大成功')

      # with open('point.json', 'r+', encoding='utf8') as jfile:
      #   jpoint = json.load(jfile)
      #   username = str(msg.author)
      #   if(username not in jpoint):
      #     dd = {username:10}
      #     jpoint.update(dd)
      #     jfile.seek(0)
      #     json.dump(jpoint, jfile)
      #     return
      #   else:
      #     user_point = jpoint[username] + 10
      #     dd = {username:user_point}       
      #     jpoint.update(dd)
      #     jfile.seek(0)
      #     json.dump(jpoint, jfile)
      #     return


def setup(bot):
    bot.add_cog(Event(bot))
