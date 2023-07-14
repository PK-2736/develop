from discord.ext import tasks, commands
import discord
from discord.commands import slash_command, Option
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from datetime import datetime
import requests
import json
from discord.ext import pages
from cogs import guild_ids
import io

print("coopstageの読み込み完了")

class coopstage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.loop.start()

    @tasks.loop(seconds=60)
    async def loop(self):
            url = "https://spla3.yuu26.com/api/coop-grouping-regular/schedule"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}

            response = requests.get(url)
            jsonData = response.json()

            salmon_map   = jsonData["results"][1]["stage"]["name"]
            salmon_img_1 = jsonData["results"][1]["weapons"][0]["image"]
            salmon_img_2 = jsonData["results"][1]["weapons"][1]["image"]
            salmon_img_3 = jsonData["results"][1]["weapons"][2]["image"]
            salmon_img_4 = jsonData["results"][1]["weapons"][3]["image"]
            image = jsonData["results"][1]["stage"]["image"]

            time = jsonData["results"][1]["start_time"]
            time2 = jsonData["results"][1]["end_time"]
            t = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
            n = t.strftime('%m/%d %H:%M')
            t2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S%z')
            n2 = t2.strftime('%m/%d %H:%M')
            img = Image.new('RGBA', (720,580), (44, 47, 51))
            im1 = Image.open(io.BytesIO(requests.get(salmon_img_1).content))
            im2 = Image.open(io.BytesIO(requests.get(salmon_img_2).content))
            im3 = Image.open(io.BytesIO(requests.get(salmon_img_3).content))
            im4 = Image.open(io.BytesIO(requests.get(salmon_img_4).content))
            im5 = Image.open(io.BytesIO(requests.get(image).content))
            im1.thumbnail((180,180))
            im2.thumbnail((180,180))
            im3.thumbnail((180,180))
            im4.thumbnail((180,180))
            im5.thumbnail((720,600))
            img_binary = io.BytesIO()
            img.paste(im1, (0,0))
            img.paste(im2, (180,0))
            img.paste(im3, (360,0))
            img.paste(im4, (540,0))
            img.paste(im5, (0,180))
            img.save(img_binary, format='PNG')
            img_binary.seek(0)

            file = discord.File(img_binary, filename='image.png')

            salmon_embed = discord.Embed(
                                        title = "現在のサーモンラン",
                                        color = 0xff7f50,
                                        description=f"**{n}から{n2}まで**\n\n**{salmon_map}**\n\n**-支給武器-**")
            salmon_embed.set_image(url="attachment://image.png")
            salmon_embed.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/thumb/1/13/S2_Band_Grizzco_Industries.jpg/251px-S2_Band_Grizzco_Industries.jpg")
            salmon_embed.set_footer(text="API: https://spla3.yuu26.com| イカコード3")

            now = datetime.now().strftime('%H:%M')
            if now == '09:01' or now == '17:01' or now == '01:01':
                channel = self.bot.get_channel(1031555972109455373)
                await channel.send(embed=salmon_embed,file=file)   

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return

        if message.content.lower() in ['バイト', 'ばいと', 'サーモン', 'さーもん', 'サモラン', 'サーモンラン', 'さーもんらん', 'しゃけ', 'シャケ', 'coop', 'salmonrun']:
            url = "https://spla3.yuu26.com/api/coop-grouping-regular/schedule"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}

            response = requests.get(url)
            jsonData = response.json()

            salmon_map   = jsonData["results"][0]["stage"]["name"]
            salmon_img_1 = jsonData["results"][0]["weapons"][0]["image"]
            salmon_img_2 = jsonData["results"][0]["weapons"][1]["image"]
            salmon_img_3 = jsonData["results"][0]["weapons"][2]["image"]
            salmon_img_4 = jsonData["results"][0]["weapons"][3]["image"]
            image = jsonData["results"][0]["stage"]["image"]

            time = jsonData["results"][0]["start_time"]
            time2 = jsonData["results"][0]["end_time"]
            t = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
            n = t.strftime('%m/%d %H:%M')
            t2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S%z')
            n2 = t2.strftime('%m/%d %H:%M')
            img = Image.new('RGBA', (720,580), (44, 47, 51))
            im1 = Image.open(io.BytesIO(requests.get(salmon_img_1).content))
            im2 = Image.open(io.BytesIO(requests.get(salmon_img_2).content))
            im3 = Image.open(io.BytesIO(requests.get(salmon_img_3).content))
            im4 = Image.open(io.BytesIO(requests.get(salmon_img_4).content))
            im5 = Image.open(io.BytesIO(requests.get(image).content))
            im1.thumbnail((180,180))
            im2.thumbnail((180,180))
            im3.thumbnail((180,180))
            im4.thumbnail((180,180))
            im5.thumbnail((720,600))
            img_binary = io.BytesIO()
            img.paste(im1, (0,0))
            img.paste(im2, (180,0))
            img.paste(im3, (360,0))
            img.paste(im4, (540,0))
            img.paste(im5, (0,180))
            img.save(img_binary, format='PNG')
            img_binary.seek(0)

            file = discord.File(img_binary, filename='image.png')

            salmon_embed = discord.Embed(
                                        title = "サーモンラン",
                                        color = 0xff7f50,
                                        description=f"**{n}から{n2}まで**\n\n**{salmon_map}**\n\n**-支給武器-**")
            salmon_embed.set_image(url="attachment://image.png")
            salmon_embed.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/thumb/1/13/S2_Band_Grizzco_Industries.jpg/251px-S2_Band_Grizzco_Industries.jpg")
            salmon_embed.set_footer(text="API: https://spla3.yuu26.com| イカコード3")
            ctx = await self.bot.get_context(message)

            await ctx.send(embed=salmon_embed,file=file)   

        if message.content.lower() in ['次のバイト', 'つぎのばいと', '次のサーモン', 'つぎのさーもん', '次のサモラン', '次のサーモンラン', 'つぎのさーもんらん', 'つぎのしゃけ', '次のシャケ', 'nextcoop', 'nextsalmonrun']:

            url = "https://spla3.yuu26.com/api/coop-grouping-regular/schedule"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}

            response = requests.get(url)
            jsonData = response.json()

            salmon_map   = jsonData["results"][1]["stage"]["name"]
            salmon_img_1 = jsonData["results"][1]["weapons"][0]["image"]
            salmon_img_2 = jsonData["results"][1]["weapons"][1]["image"]
            salmon_img_3 = jsonData["results"][1]["weapons"][2]["image"]
            salmon_img_4 = jsonData["results"][1]["weapons"][3]["image"]
            image = jsonData["results"][1]["stage"]["image"]

            time = jsonData["results"][1]["start_time"]
            time2 = jsonData["results"][1]["end_time"]
            t = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
            n = t.strftime('%m/%d %H:%M')
            t2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S%z')
            n2 = t2.strftime('%m/%d %H:%M')
            img = Image.new('RGBA', (720,580), (44, 47, 51))
            im1 = Image.open(io.BytesIO(requests.get(salmon_img_1).content))
            im2 = Image.open(io.BytesIO(requests.get(salmon_img_2).content))
            im3 = Image.open(io.BytesIO(requests.get(salmon_img_3).content))
            im4 = Image.open(io.BytesIO(requests.get(salmon_img_4).content))
            im5 = Image.open(io.BytesIO(requests.get(image).content))
            im1.thumbnail((180,180))
            im2.thumbnail((180,180))
            im3.thumbnail((180,180))
            im4.thumbnail((180,180))
            im5.thumbnail((720,600))
            img_binary = io.BytesIO()
            img.paste(im1, (0,0))
            img.paste(im2, (180,0))
            img.paste(im3, (360,0))
            img.paste(im4, (540,0))
            img.paste(im5, (0,180))
            img.save(img_binary, format='PNG')
            img_binary.seek(0)

            file2 = discord.File(img_binary, filename='image.png')

            salmon_embed1 = discord.Embed(
                                        title = "サーモンラン",
                                        color = 0xff7f50,
                                        description=f"**{n}から{n2}まで**\n\n**{salmon_map}**\n\n**-支給武器-**")
            salmon_embed1.set_image(url="attachment://image.png")
            salmon_embed1.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/thumb/1/13/S2_Band_Grizzco_Industries.jpg/251px-S2_Band_Grizzco_Industries.jpg")
            salmon_embed1.set_footer(text="API: https://spla3.yuu26.com| イカコード3")
            ctx = await self.bot.get_context(message)

            await ctx.send(embed=salmon_embed1,file=file2)             

    
    @slash_command(name='すてバイト', guild_ids = guild_ids, description='サーモンランのステージ情報を取得します。')
    async def coop(self, ctx, time : Option(str, '時間', choices=["今", "次"])):
        await ctx.defer()

        if time == "今":
            url = "https://spla3.yuu26.com/api/coop-grouping-regular/schedule"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}

            response = requests.get(url)
            jsonData = response.json()

            salmon_map   = jsonData["results"][0]["stage"]["name"]
            salmon_img_1 = jsonData["results"][0]["weapons"][0]["image"]
            salmon_img_2 = jsonData["results"][0]["weapons"][1]["image"]
            salmon_img_3 = jsonData["results"][0]["weapons"][2]["image"]
            salmon_img_4 = jsonData["results"][0]["weapons"][3]["image"]
            image = jsonData["results"][0]["stage"]["image"]

            time = jsonData["results"][0]["start_time"]
            time2 = jsonData["results"][0]["end_time"]
            t = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
            n = t.strftime('%m/%d %H:%M')
            t2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S%z')
            n2 = t2.strftime('%m/%d %H:%M')
            img = Image.new('RGBA', (720,580), (44, 47, 51))
            im1 = Image.open(io.BytesIO(requests.get(salmon_img_1).content))
            im2 = Image.open(io.BytesIO(requests.get(salmon_img_2).content))
            im3 = Image.open(io.BytesIO(requests.get(salmon_img_3).content))
            im4 = Image.open(io.BytesIO(requests.get(salmon_img_4).content))
            im5 = Image.open(io.BytesIO(requests.get(image).content))
            im1.thumbnail((180,180))
            im2.thumbnail((180,180))
            im3.thumbnail((180,180))
            im4.thumbnail((180,180))
            im5.thumbnail((720,600))
            img_binary = io.BytesIO()
            img.paste(im1, (0,0))
            img.paste(im2, (180,0))
            img.paste(im3, (360,0))
            img.paste(im4, (540,0))
            img.paste(im5, (0,180))
            img.save(img_binary, format='PNG')
            img_binary.seek(0)

            file = discord.File(img_binary, filename='image.png')

            salmon_embed = discord.Embed(
                                        title = "サーモンラン",
                                        color = 0xff7f50,
                                        description=f"**{n}から{n2}まで**\n\n**{salmon_map}**\n\n**-支給武器-**")
            salmon_embed.set_image(url="attachment://image.png")
            salmon_embed.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/thumb/1/13/S2_Band_Grizzco_Industries.jpg/251px-S2_Band_Grizzco_Industries.jpg")
            salmon_embed.set_footer(text="API: https://spla3.yuu26.com| イカコード3")

            await ctx.respond(embed=salmon_embed,file=file,ephemeral = True)

        if time == "次":
            url = "https://spla3.yuu26.com/api/coop-grouping-regular/schedule"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}

            response = requests.get(url)
            jsonData = response.json()

            salmon_map   = jsonData["results"][1]["stage"]["name"]
            salmon_img_1 = jsonData["results"][1]["weapons"][0]["image"]
            salmon_img_2 = jsonData["results"][1]["weapons"][1]["image"]
            salmon_img_3 = jsonData["results"][1]["weapons"][2]["image"]
            salmon_img_4 = jsonData["results"][1]["weapons"][3]["image"]
            image = jsonData["results"][1]["stage"]["image"]

            time = jsonData["results"][1]["start_time"]
            time2 = jsonData["results"][1]["end_time"]
            t = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
            n = t.strftime('%m/%d %H:%M')
            t2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S%z')
            n2 = t2.strftime('%m/%d %H:%M')
            img = Image.new('RGBA', (720,580), (44, 47, 51))
            im1 = Image.open(io.BytesIO(requests.get(salmon_img_1).content))
            im2 = Image.open(io.BytesIO(requests.get(salmon_img_2).content))
            im3 = Image.open(io.BytesIO(requests.get(salmon_img_3).content))
            im4 = Image.open(io.BytesIO(requests.get(salmon_img_4).content))
            im5 = Image.open(io.BytesIO(requests.get(image).content))
            im1.thumbnail((180,180))
            im2.thumbnail((180,180))
            im3.thumbnail((180,180))
            im4.thumbnail((180,180))
            im5.thumbnail((720,600))
            img_binary = io.BytesIO()
            img.paste(im1, (0,0))
            img.paste(im2, (180,0))
            img.paste(im3, (360,0))
            img.paste(im4, (540,0))
            img.paste(im5, (0,180))
            img.save(img_binary, format='PNG')
            img_binary.seek(0)

            file2 = discord.File(img_binary, filename='image.png')

            salmon_embed = discord.Embed(
                                        title = "サーモンラン",
                                        color = 0xff7f50,
                                        description=f"**{n}から{n2}まで**\n\n**{salmon_map}**\n\n**-支給武器-**")
            salmon_embed.set_image(url="attachment://image.png")
            salmon_embed.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/thumb/1/13/S2_Band_Grizzco_Industries.jpg/251px-S2_Band_Grizzco_Industries.jpg")
            salmon_embed.set_footer(text="API: https://spla3.yuu26.com| イカコード3")

            await ctx.respond(embed=salmon_embed,file=file2,ephemeral = True)

def setup(bot):
    bot.add_cog(coopstage(bot))