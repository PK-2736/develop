import discord
from discord.ext import commands
import asyncio
import sys
import sqlite3
import datetime
from datetime import timezone, tzinfo, timedelta
from discord.commands import slash_command, Option
from cogs import guild_ids
import re

print("fcの読み込み完了")

class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(style=discord.ButtonStyle.red,label="削除",custom_id="rm") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction: discord.Interaction):
        await interaction.message.delete()

class friendcode(commands.Cog, name='friendcode'):
    
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
               
    @slash_command(name="ふれこ登録", guild_ids=guild_ids, description="自分のフレンドコードをセットします。")
    async def addcode(self, interaction: discord.Interaction, *, friendcode: Option(str, "例：1111-1111-1111")):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        
        cursor.execute(f"SELECT user_id FROM friendcode WHERE guild_id = '{interaction.guild.id}' and user_id = '{interaction.user.id}'")
        result = cursor.fetchone()

        if result is None:
            sql = ("INSERT INTO friendcode(guild_id, user_id, friendcode) VALUES(?,?,?)")
            val = (interaction.guild.id, interaction.user.id, friendcode)
            embed = discord.Embed( 
            color=0xf09214, 
            description=f"フレンドコードを登録しました。\n`{friendcode}`")
            await interaction.response.send_message(embed=embed,delete_after=10)

            embed2 = discord.Embed( 
            color=0xf09214,
            description=f"{interaction.user.mention} がフレンドコードを設定しました。\n`{friendcode}`" )
            channel = self.bot.get_channel(1028366913140703243)
            await channel.send(embed=embed2) 

        elif result is not None:
            sql = ('UPDATE main.friendcode SET friendcode = ? WHERE user_id = ?')
            val = (friendcode, interaction.user.id)
            embed = discord.Embed( 
            color=0xf09214, 
            description=f"フレンドコードを再登録しました。\n`{friendcode}`")
            await interaction.response.send_message(embed=embed,delete_after=10)

            embed2 = discord.Embed( 
            color=0xf09214,
            description=f"{interaction.user.mention} がフレンドコードを再設定しました。\n`{friendcode}`" )
            channel = self.bot.get_channel(1028366913140703243)
            await channel.send(embed=embed2) 

        cursor.execute(sql, val)
        db.commit()  
        cursor.close()
        db.close()
                   
    @slash_command(name="ふれこ検索", guild_ids=guild_ids, description="特定の人のフレンドコードを表示します。")
    async def search(self, interaction: discord.Interaction, user:discord.User=None):

        if user is not None:
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT friendcode FROM friendcode WHERE guild_id = '{interaction.guild.id}' and user_id = '{user.id}'")
            result = cursor.fetchone()

            if result is None:
                embed = discord.Embed(colour=0xcf5547, description=f"{user.name}はフレンドコードを登録していません。")
                await interaction.response.send_message(embed=embed,ephemeral = True)
            else:
                embed = discord.Embed(colour=0xEAFF15, title=f"{user.name}さんのフレンドコード\n`{str(result[0])}`")
                embed.set_footer(text=f"リクエスト：{interaction.user.name}",icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
                await interaction.response.send_message(embed=embed,view=MyView(), delete_after=1000)

            cursor.close()
            db.close()

        elif user is None:
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT friendcode FROM friendcode WHERE guild_id = '{interaction.guild.id}' and user_id = '{interaction.user.id}'")
            result = cursor.fetchone()

            if result is None:
                embed = discord.Embed(colour=0xcf5547, description=f"{interaction.user.name}はフレンドコードを登録していません。")
                await interaction.response.send_message(embed=embed,ephemeral = True)
            else:
                embed = discord.Embed(colour=0xEAFF15, title=f"{interaction.user.name}さんのフレンドコード\n`{str(result[0])}`")
                embed.set_footer(text=f"リクエスト：{interaction.user.name}",icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
                await interaction.response.send_message(embed=embed,view=MyView(), delete_after=1000)
            cursor.close()
            db.close()

    @commands.Cog.listener()
    async def on_message(self, message): 
        if message.channel.id not in [802345513495822339,982600148259602442,1028366913140703243]:
                return
        if message.author.bot:
                return
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        discordname = message.author.mention
        words=['/fc登録']
        for word in words:
                if word in message.content:
                    before_words = message.content
                    after_words = re.search(r'(\d{4})-?(\d{4})-?(\d{4})', before_words)
                    if after_words:

                        cursor.execute(f"SELECT user_id FROM friendcode WHERE guild_id = '{message.author.guild.id}' and user_id = '{message.author.id}'")
                        result = cursor.fetchone()

                        if result is None:
                            sql = ("INSERT INTO friendcode(guild_id, user_id, friendcode) VALUES(?,?,?)")
                            val = (message.author.guild.id, message.author.id, after_words.group(0))
                            embed = discord.Embed( 
                            color=0xf09214, 
                            description=f"フレンドコードを登録しました。\n`{after_words.group(0)}`")
                            await message.channel.send(embed=embed,delete_after=10)

                            embed2 = discord.Embed( 
                            color=0xf09214, 
                            description=f"{discordname} がフレンドコードを設定しました {after_words.group(0)}"
                            )
                            channel = self.bot.get_channel(1028366913140703243)
                            await channel.send(embed=embed2) 

                        elif result is not None:
                            sql = ('UPDATE main.friendcode SET friendcode = ? WHERE user_id = ?')
                            val = (after_words.group(0), message.author.id)
                            embed = discord.Embed( 
                            color=0xf09214, 
                            description=f"フレンドコードを再登録しました。\n`{after_words.group(0)}`")
                            await message.channel.send(embed=embed,delete_after=10)

                            embed2 = discord.Embed( 
                            color=0xf09214, 
                            description=f"{discordname} がフレンドコードを再設定しました {after_words.group(0)}" 
                            )
                            channel = self.bot.get_channel(1028366913140703243)
                            await channel.send(embed=embed2) 

                        cursor.execute(sql, val)
                        db.commit()
                    else:
                        embed = discord.Embed(
                        color=0xcf5547, 
                        description=f'適切なフレンドコードを入力して下さい。\n再入力は`/fc登録`で確認出来ます。'
                                            )
                        await message.channel.send(embed=embed, delete_after=10)

    @slash_command(name="ふれこ削除", guild_ids=guild_ids, description="フレンドコードを削除します。")
    async def delete(self, interaction: discord.Interaction, friendcode: Option(str, "例：1111-1111-1111")):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT user_id FROM friendcode WHERE guild_id = '{interaction.guild.id}' and user_id = '{interaction.user.id}'")
        result = cursor.fetchone()

        if result is None:
            embed = discord.Embed(
            color=0xcf5547, 
            description=f'フレンドコードを登録してない、またはフレンドコードが間違っています。\n入力したフレンドコード: `{friendcode}`')
            await interaction.response.send_message(embed=embed, ephemeral=True)

        elif result is not None:
            embed = discord.Embed(
            color=0xcf5547, 
            description=f'フレンドコードを削除しました。\n`{friendcode}`')
            await interaction.response.send_message(embed=embed, delete_after=10)
            sql = (f"DELETE FROM main.friendcode WHERE guild_id = '{interaction.guild.id}' and user_id = '{interaction.user.id}' and friendcode = '{friendcode}'")

            embed2 = discord.Embed( 
            color=0xcf5547, 
            description=f"{interaction.user.mention} がフレンドコードを削除しました。\n`{friendcode}`" )
            channel = self.bot.get_channel(1028366913140703243)
            await channel.send(embed=embed2) 

            cursor.execute(sql)
            db.commit()  
        cursor.close()
        db.close()
       
def setup(bot):
    bot.add_cog(friendcode(bot))