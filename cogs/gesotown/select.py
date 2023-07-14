import discord
from discord.ext import tasks, commands
from discord.commands import slash_command, Option
from datetime import datetime
import requests
from cogs import guild_ids
import sqlite3
import re

print("gesoeveの読み込み完了")

class select(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.loop1.start()

    @slash_command(name='ギア登録',guild_ids=guild_ids, description='ギア登録')
    async def selectgear(self, interaction: discord.Interaction, time : Option(str, '時間', choices=["1つ目", "2つ目", "3つ目"]),brand : Option(str,required=False,description="ブランド"), gear : Option(str,required=False,description="ギア"), power : Option(str,required=False,description="メインパワー")):
                      
        if time == "1つ目":  
            db = sqlite3.connect('geso.sqlite')
            cursor = db.cursor()
            
            cursor.execute(f"SELECT user_id FROM geso WHERE guild_id = '{interaction.guild.id}' and user_id = '{interaction.user.id}'")
            result = cursor.fetchone()
            
        if result is None:
            sql = ("INSERT INTO geso(guild_id, user_id, brand, gear, power) VALUES(?,?,?,?,?)")
            val = (interaction.guild.id, interaction.user.id, brand, gear, power)
            embed = discord.Embed( 
            color=0xf09214, 
            description=f"ギアを登録しました！販売されたらDMに報告します！\n`{brand}`\n`{gear}`\n`{power}`")
            await interaction.response.send_message(embed=embed,delete_after=10)

            # embed2 = discord.Embed( 
            # color=0xf09214,
            # description=f"{interaction.user.mention} がフレンドコードを設定しました。\n`{geso}`" )
            # channel = self.bot.get_channel(1028366913140703243)
            # await channel.send(embed=embed2) 

        elif result is not None:
            sql = ('UPDATE main.geso SET brand=?, gear=?, power=? WHERE user_id = ?')
            val = (brand, gear, power, interaction.user.id)
            embed = discord.Embed( 
            color=0xf09214, 
            description=f"ギアを登録しました。\n`{brand}`\n`{gear}`\n`{power}`")
            await interaction.response.send_message(embed=embed,delete_after=10)

            # embed2 = discord.Embed( 
            # color=0xf09214,
            # description=f"{interaction.user.mention} がフレンドコードを再設定しました。\n`{geso}`" )
            # channel = self.bot.get_channel(1028366913140703243)
            # await channel.send(embed=embed2) 
            # cursor.execute(sql, val)

        if time == "2つ目":
            db = sqlite3.connect('geso.sqlite')
            cursor = db.cursor()
            
            cursor.execute(f"SELECT user_id FROM geso WHERE guild_id = '{interaction.guild.id}' and user_id = '{interaction.user.id}'")
            result = cursor.fetchone()  

        if time == "3つ目":
            db = sqlite3.connect('geso.sqlite')
            cursor = db.cursor()
            
            cursor.execute(f"SELECT user_id FROM geso WHERE guild_id = '{interaction.guild.id}' and user_id = '{interaction.user.id}'")
            result = cursor.fetchone() 

        cursor.execute(sql, val)
        db.commit()  
        cursor.close()
        db.close()


    
    @slash_command(name='ギア確認',guild_ids=guild_ids, description='ギア確認')
    async def checkgear(self, interaction: discord.Interaction):

        db = sqlite3.connect('geso.sqlite')
        cursor = db.cursor()
        sql = 'select * from geso'
        for row in cursor.execute(sql):
                result = (str(row[2]) + "," + str(row[3]))
                print(result)
                embed = discord.Embed( 
                color=0xf09214, 
                description=f"ギア内容：\n`{result}\n{row}`")
                await interaction.response.send_message(embed=embed)

    @tasks.loop(seconds=60)
    async def loop1(self):

        url = "https://splatoon3.ink/data/gear.json"
        response = requests.get(url)
        jsonData = response.json()
        image = jsonData["data"]["gesotown"]["pickupBrand"]["brandGears"][0]["gear"]["image"]["url"]

        url2 = "https://api.koukun.jp/splatoon/3/geso/"
        ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
        headers = {"User-Agent": ua}
        response = requests.get(url2)
        jsonData = response.json()
        btime = jsonData["pickupBrand"]["saleEndTime"]
        t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
        n = t.strftime('%m/%d %H:%M')
        gear = jsonData["pickupBrand"]["brandGears"][0]["gear"]["name"]
        brand = jsonData["pickupBrand"]["brandGears"][0]["gear"]["brand"]["name"]
        bgearpower = jsonData["pickupBrand"]["brandGears"][0]["gear"]["primaryGearPower"]
        price = jsonData["pickupBrand"]["brandGears"][0]["price"]

        now = datetime.now().strftime('%H:%M')
        if now == '09:01':
            channel = self.bot.get_channel(1043379022685536256)
            await channel.send()

def setup(bot):
    bot.add_cog(select(bot))