import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import pyopenjtalk, numpy
from scipy.io import wavfile
import numpy as np
from cogs import guild_ids
import re

class TTS(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @slash_command(name="せつぞく",guild_ids=guild_ids,description="読み上げをボイスチャンネルに接続させます。")
    async def join(selh,ctx):
      vc = ctx.author.voice.channel
      await vc.connect()
      await ctx.respond("ボイスチャンネルに接続しました。")
      with open('data/voice.txt', 'w') as f:
        f.write(f'{ctx.channel.id}')

    @slash_command(name="せつだん",guild_ids=guild_ids,description="読み上げをボイスチャンネルから切断させます。")
    async def bye(selh,ctx):
      await ctx.voice_client.disconnect()
      await ctx.respond("ボイスチャンネルから切断しました。")

    @commands.Cog.listener()
    async def on_message(selh,message):
      with open('data/voice.txt', 'r') as f:
        voiceid = f.read()
        match = re.fullmatch(f"{message.channel.id}",voiceid)

      if match:

        if message.guild.voice_client:
          x, sr = pyopenjtalk.tts(message.content)
          wavfile.write("test.wav", sr, x.astype(np.int16))
          source = discord.FFmpegPCMAudio("test.wav")
          message.guild.voice_client.play(source)

def setup(bot):
    bot.add_cog(TTS(bot))