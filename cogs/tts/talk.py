import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import pyopenjtalk, numpy
from scipy.io import wavfile
import numpy as np
from cogs import guild_ids
import re
from datetime import datetime
from discord.utils import get


class TTS(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @slash_command(name="せつぞく",guild_ids=guild_ids,description="読み上げをボイスチャンネルに接続させます。")
    async def join(self,ctx: discord.ApplicationContext):

      if ctx.author.voice == None:
            embed = discord.Embed(
            timestamp=datetime.now(),
            color=0xdd4a4a,
            title="ボイスチャンネルに接続してください。"
        )
            await ctx.respond(embed=embed,ephemeral = True)
      
      else:
        vc = ctx.author.voice.channel
        await vc.connect()
        embed = discord.Embed(
              timestamp=datetime.now(),
              color=0x71177e,
              title="ボイスチャンネルに接続しました。",
              description=f"発言可能なテキストチャンネル\n{ctx.author.voice.channel.mention}・{ctx.channel.mention}"#・{ctx.message.channel.mention}"
          )
        await ctx.respond(embed=embed)
        with open('data/voice.txt', 'w') as f:
          f.write(f'{ctx.channel.id}{ctx.author.voice.channel.id}')

        x, sr = pyopenjtalk.tts("ボイスチャンネルに接続しました")
        wavfile.write("test.wav", sr, x.astype(np.int16))
        source = discord.FFmpegPCMAudio("test.wav")
        ctx.guild.voice_client.play(source)
        await ctx.guild.change_voice_state(channel=ctx.author.voice.channel,self_deaf=True)


    @slash_command(name="せつだん",guild_ids=guild_ids,description="読み上げをボイスチャンネルから切断させます。")
    async def bye(self,ctx: discord.ApplicationContext):

      if ctx.author.voice == None:
            embed = discord.Embed(
            timestamp=datetime.now(),
            color=0xdd4a4a,
            title="ボイスチャンネルに接続してください。"
        )
            await ctx.respond(embed=embed,ephemeral = True)
      
      else:
        embed = discord.Embed(
              timestamp=datetime.now(),
              color=0xdd4a4a,
              title="ボイスチャンネルから切断しました。"
          )
        await ctx.respond(embed=embed)
        await ctx.voice_client.disconnect()

    @commands.Cog.listener()
    async def on_message(selh,message: discord.Message):

      if message.author.bot:
        return

      with open('data/voice.txt', 'r') as f:
        voiceid = f.read()
        match = re.fullmatch(f"{message.channel.id}{message.author.voice.channel.id}",voiceid)

      if match:

          if message.guild.voice_client:

            messagestr = message.content
            url = re.search(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+",messagestr)
            role = re.search(r"<@&[0-9]+>", messagestr)
            member = re.search(r"<@[0-9]+>", messagestr)

            if url:
              messagestr = messagestr.replace(url.group(), "以下URL省略")
              x, sr = pyopenjtalk.tts(messagestr)
              wavfile.write("test.wav", sr, x.astype(np.int16))
              source = discord.FFmpegPCMAudio("test.wav")
              message.guild.voice_client.play(source)
              return

            elif role:
              messagestr = messagestr.replace(role.group(), "役職メンション")
              x, sr = pyopenjtalk.tts(messagestr)
              wavfile.write("test.wav", sr, x.astype(np.int16))
              source = discord.FFmpegPCMAudio("test.wav")
              message.guild.voice_client.play(source)
              return

            elif member:
              for a in message.mentions:
                  text = message.content
                  text = text.replace(f'<@!{a.id}>', f'メンション{a.display_name}さん')
                  text = text.replace(f'<@{a.id}>', f'メンション{a.display_name}さん')
                  x, sr = pyopenjtalk.tts(text)
                  wavfile.write("test.wav", sr, x.astype(np.int16))
                  source = discord.FFmpegPCMAudio("test.wav")
                  message.guild.voice_client.play(source)
                  return
              
            #TODO リプライへの反応 
            # elif message.:
            #       x, sr = pyopenjtalk.tts(f"リプライ{message.content}")
            #       wavfile.write("test.wav", sr, x.astype(np.int16))
            #       source = discord.FFmpegPCMAudio("test.wav")
            #       message.guild.voice_client.play(source)
            #       return

            else:
              x, sr = pyopenjtalk.tts(message.content)
              wavfile.write("test.wav", sr, x.astype(np.int16))
              source = discord.FFmpegPCMAudio("test.wav")
              message.guild.voice_client.play(source)

def setup(bot):
    bot.add_cog(TTS(bot))