from discord.ext import commands
import discord
import datetime
from discord.ui import View, Button
from discord.ext import commands
from cogs import guild_ids
from discord.commands import slash_command, Option

print("clientの読み込み完了")

class client(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @slash_command(name="ikacord",guild_ids=guild_ids, description="BOTの情報表示")
    async def client_info(self, ctx):
        client = self.bot
        raw_ping = self.bot.latency
        ping = round(raw_ping * 1000)
        app_info = await client.application_info()
        embed = discord.Embed(title="ikacord bot情報",description=f"ping: {ping}\n"
            f"Botユーザー名: {client.user.name}\n"
            f"BotユーザーID: {client.user.id}\n"
            f"Guild数: {len(client.guilds)}\n"
            f"ボイス接続数: {len(client.voice_clients)}\n"
            f"ユニークユーザー数: {len(client.users)}\n"
            f"延べユーザー数: {sum([g.member_count for g in client.guilds])}\n"
            f"アプリケーションID: {app_info.id}\n"
            f"Botオーナー: {app_info.owner.name}\n"
            f"Public Bot?: {app_info.bot_public}\n",color=discord.Color.blurple(),timestamp=datetime.datetime.now())
        await ctx.respond(embed=embed)
        
def setup(bot):
    bot.add_cog(client(bot))