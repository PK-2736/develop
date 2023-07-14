import discord
import asyncio
from discord.ext import commands,tasks
import datetime
import re
from discord.commands import slash_command, Option
from cogs import guild_ids
import re

print("eventの読み込み完了")

class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
      def __init__(self):
        super().__init__()
        ServerButton1 = discord.ui.Button(label='ルールを読む', emoji='📜',style=discord.ButtonStyle.primary, url='https://discord.com/channels/981474117020712970/1022072333978058802')
        ServerButton2 = discord.ui.Button(label='サーバー説明を読む', emoji='📚',style=discord.ButtonStyle.primary, url='https://discord.com/channels/981474117020712970/1022072333978058802')
        self.add_item(ServerButton1)
        self.add_item(ServerButton2)

class event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.loop.start()

    @commands.Cog.listener()
    async def on_ready(self):
        while True:
            client = self.bot
            await client.change_presence(activity = discord.Activity(name="Help:/help", type=discord.ActivityType.playing))
            await asyncio.sleep(15)
            await client.change_presence(activity = discord.Activity(name="splatoon3", type=discord.ActivityType.playing))
            await asyncio.sleep(15)
            joinserver=len(client.guilds)
            servers=str(joinserver)
            await client.change_presence(activity = discord.Activity(name="サーバー数:"+servers, type=discord.ActivityType.playing))
            await asyncio.sleep(15)
            await client.change_presence(activity = discord.Activity(name="botについての連絡はPheyK#1280", type=discord.ActivityType.playing))
            await asyncio.sleep(15)

    @commands.Cog.listener()
    async def on_member_join(self,member: discord.Member):
        channel = self.bot.get_channel(982580316894015530)
        embed = discord.Embed( 
                        title=f"{member.name}が入室しました！",
                        description="まずは<#982600148259602442>を書こう！\n"
                                            "<#982580781589331998> で必要なロールを取得しよう！\n"
                                            "(最初の14日間は新規ロールが付与されます。)",

                        color=0x00ff00,) 
        await channel.send(embed=embed,view=MyView())

        guild = self.bot.get_guild(981474117020712970)
        role = guild.get_role(1034460174670368769)
        await member.add_roles(role)

        dt1 = datetime.datetime.now().date()
        dt2 = dt1 + datetime.timedelta(days=14)
        file = open("data/join.txt", "a")
        file.write(f'{member.id} {dt2}\n')
        file.close()

    @tasks.loop(hours=24)
    async def loop(self):
        searchfile = open("data/join.txt")
        dt_now = datetime.datetime.now().date()

        for line in searchfile:
            if f'{dt_now}' in line:
                search = re.search(r'\d{18}', line)
                user_id = search.group(0)
                if f'{user_id} {dt_now}' in line: 
                    guild = self.bot.get_guild(981474117020712970)
                    role = guild.get_role(1034460174670368769)

                    if {user_id} in {guild}:
                        input_date = int(user_id)
                        user = guild.get_member(input_date)
                        await user.remove_roles(role)

                        
                        with open("data/join.txt", "r") as f:
                            lines = f.readlines()
                        with open("data/join.txt", "w") as f:
                                for line in lines:
                                    if line.strip("\n") != f'{input_date} {dt_now}':
                                        f.write(line)
                    
                    else:
                        global input_date1
                        input_date1 = int(user_id)
                        with open("data/join.txt", "r") as f:
                            lines = f.readlines()
                        with open("data/join.txt", "w") as f:
                                for line in lines:
                                    if line.strip("\n") != f'{input_date1} {dt_now}':
                                        f.write(line)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(982596256868225054)
        await channel.send(f"{member.name}行かないで！どうしてなの！？ 私を置いていかないで！")

    # @commands.Cog.listener()
    # async def on_application_command_error(
    #     self, ctx: discord.ApplicationContext, error: discord.ApplicationCommandError
    #         ):
    #     if isinstance(error, discord.ApplicationCommandInvokeError):
    #             embed = discord.Embed(
    #                 color=0xe64b47,
    #                 description="コマンドエラー"
    #                 )
    #             await ctx.send(embed=embed, reference=ctx.message)
    #     else:
    #             raise error
    
def setup(bot):
    bot.add_cog(event(bot))