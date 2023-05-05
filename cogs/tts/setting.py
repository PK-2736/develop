import discord
from discord.ext import commands
from discord import SlashCommandGroup, ApplicationContext, Option, StageChannel, TextChannel, VoiceChannel
from discord.commands import slash_command, Option
from cogs import guild_ids
import re
from datetime import datetime
import threading
import os
import json
import requests

print("settingの読み込み完了")

class set(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @slash_command(name="りみっと", description="ユーザーの制限数を設定します。",guild_ids=guild_ids)
    async def VoiceSettings_Limit(self, ctx : ApplicationContext, channel : Option(VoiceChannel, "制限をつけるチャンネルを選択"), limit : Option(int, "制限人数を入力（0にすると制限解除）")):
        if ctx.author.voice == None:
            embed = discord.Embed(
            timestamp=datetime.now(),
            color=0xdd4a4a,
            title="ボイスチャンネルに接続してください。"
        )
            await ctx.respond(embed=embed,ephemeral = True)

        else:
            await ctx.defer()
            embed = discord.Embed(title=f"{channel.name} の制限を設定しました。\n制限は二時間後に自動で解除されます。", description=f"制限解除をする場合はコマンドのlimitを0にしてください。\n{channel.user_limit} -> {limit} 人", color=discord.Color.green(),timestamp=datetime.now())
            await channel.edit(user_limit=limit)
            await ctx.respond(embed=embed)
            async def limits():
                i = 0
                while True:
                    print("\r{}:".format(i), end="")
                    i += 1
                    event = threading.Event()
                    if event.wait(timeout=7200):
                        await channel.edit(user_limit=0)
                        break

                th = threading.Thread(target=limits)
                th.start()
                input()
                event.set()

    @slash_command(name="じしょとうろく", description="読み上げを行うときの辞書を設定します。",guild_ids=guild_ids)
    async def dict(self, ctx : ApplicationContext,  word : Option(str,"単語"), read : Option(str,"読み")):
        # words = {}

        # words[word] = read
        # with open(f"./dict.json", "w", encoding="UTF-8")as f:
        #         f.write(json.dumps(words, indent=2, ensure_ascii=False))
        # dict_add_embed = discord.Embed(title="辞書追加", color=0x3399cc)
        # dict_add_embed.add_field(name="単語", value=f"{word}", inline="false")
        # dict_add_embed.add_field(name="読み", value=f"{read}", inline="false")
        a = discord.Embed(title="開発中です", color=0x3399cc)
        await ctx.respond(embed=a,ephemeral = True)
    
    @slash_command(name="じしょさくじょ", description="読み上げを行うときの辞書を削除します。",guild_ids=guild_ids)
    async def dele(self, ctx : ApplicationContext,  read : Option(str,"単語")):
            # words = {}
            # del words[read]
            # with open(f"./dict.json", "w", encoding="UTF-8")as f:
            #     f.write(json.dumps(words, indent=2, ensure_ascii=False))
            # await ctx.channel.send(f"辞書から`{read}`を削除しました")
            a = discord.Embed(title="開発中です", color=0x3399cc)
            await ctx.respond(embed=a,ephemeral = True)
    
def setup(bot):
    bot.add_cog(set(bot))