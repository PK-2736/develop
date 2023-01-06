import discord
import asyncio
from discord.ext import commands

print("eventの読み込み完了")

class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
      def __init__(self):
        super().__init__()
        supportServerButton = discord.ui.Button(label='サーバー説明を読む', emoji='📚',style=discord.ButtonStyle.primary, url='https://discord.com/channels/981474117020712970/1022072333978058802')
        self.add_item(supportServerButton)

class event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
    async def on_member_join(self, member):
        channel = self.bot.get_channel(982580316894015530)
        embed = discord.Embed( 
                        title=f"{member.name}が入室しました！",
                        description="まずは <#982580263936749578>を呼んで <#982600148259602442>を書きましょう！\n"
                                            "<#982580781589331998> で必要なロールを取得しよう！",
                        color=0x00ff00,) 
        await channel.send(embed=embed,view=MyView())


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(982596256868225054)
        await channel.send(f"{member.name}行かないで！どうしてなの！？ 私を置いていかないで！")


    #@commands.Cog.listener()
    async def on_application_command_error(
        self, ctx: discord.ApplicationContext, error: discord.ApplicationCommandError
            ):
        if isinstance(error, discord.ApplicationCommandInvokeError):
                embed = discord.Embed(
                    color=0xe64b47,
                    description="コマンドエラー"
                    )
                await ctx.send(embed=embed, reference=ctx.message)
        else:
                raise error
                
    @commands.Cog.listener()
    async def on_error(
        self, ctx: discord.ApplicationContext, error: discord.errors.HTTPException
            ):
        if isinstance(error, discord.errors.HTTPException):
                embed = discord.Embed(
                    color=0xe64b47,
                    description="aaaaaaaaaa"
                    )
                await ctx.send(embed=embed)
        else:
                raise error
    

def setup(bot):
    bot.add_cog(event(bot))