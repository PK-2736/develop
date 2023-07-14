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

print("gear3の読み込み完了")

class gear3(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.loop.start()
        self.loop2.start()

    @tasks.loop(seconds=60)
    async def loop(self):
            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["limitedGears"][5]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["limitedGears"][5]["gear"]["name"]
            bgearpower = jsonData["limitedGears"][5]["gear"]["primaryGearPower"]
            bprice = jsonData["limitedGears"][5]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["limitedGears"][5]["gear"]["image"]["url"]

            embed4 = discord.Embed(
                                        title = "ピックギアが追加されました",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}**￥")
            embed4.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            embed4.set_thumbnail(url=bimage)
            now = datetime.now().strftime('%H:%M')
            if now == '09:00' or now == '13:00' or now == '17:00' or now == '21:00' or now == '01:00' or now == '05:00':
                channel = self.bot.get_channel(1031555995954057317)
                await channel.send(embed=embed4)

    @tasks.loop(seconds=60)
    async def loop2(self):
            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["pickupBrand"]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["pickupBrand"]["brandGears"][0]["gear"]["name"]
            bgearpower = jsonData["pickupBrand"]["brandGears"][0]["gear"]["primaryGearPower"]
            bprice = jsonData["pickupBrand"]["brandGears"][0]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage1 = jsonData["data"]["gesotown"]["pickupBrand"]["brandGears"][0]["gear"]["image"]["url"]

            embed = discord.Embed(
                                        title = f"ブランドピックギア更新/**{n}まで**",
                                        color=0x457fce)
            embed.add_field(name=f"**{bgearname}**",value=f"**{bgearpower}**\n**{bprice}￥**")

            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["pickupBrand"]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["pickupBrand"]["brandGears"][1]["gear"]["name"]
            bgearpower = jsonData["pickupBrand"]["brandGears"][1]["gear"]["primaryGearPower"]
            bprice = jsonData["pickupBrand"]["brandGears"][1]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage2 = jsonData["data"]["gesotown"]["pickupBrand"]["brandGears"][1]["gear"]["image"]["url"]
            embed.add_field(name=f"**{bgearname}**",value=f"**{bgearpower}**\n**{bprice}￥**")

            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["pickupBrand"]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["pickupBrand"]["brandGears"][2]["gear"]["name"]
            bgearpower = jsonData["pickupBrand"]["brandGears"][2]["gear"]["primaryGearPower"]
            bprice = jsonData["pickupBrand"]["brandGears"][2]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage3 = jsonData["data"]["gesotown"]["pickupBrand"]["brandGears"][2]["gear"]["image"]["url"]
            embed.add_field(name=f"**{bgearname}**",value=f"**{bgearpower}**\n**{bprice}￥**")

            img = Image.new('RGB', (520,200), (44, 47, 51))
            im1 = Image.open(io.BytesIO(requests.get(bimage1).content))
            im2 = Image.open(io.BytesIO(requests.get(bimage2).content))
            im3 = Image.open(io.BytesIO(requests.get(bimage3).content))

            im1.thumbnail((180,180))
            im2.thumbnail((180,180))
            im3.thumbnail((180,180))
            img_binary = io.BytesIO()
            img.paste(im1, (0,0),im1)
            img.paste(im2, (180,0),im2)
            img.paste(im3, (360,0),im3)
            img.save(img_binary, format='PNG')
            img_binary.seek(0)

            file = discord.File(img_binary, filename='image.png')
            embed.set_image(url="attachment://image.png")
            embed.set_footer(text="API: https://splatoon3.ink/| イカコード3")

            now = datetime.now().strftime('%H:%M')
            if now == '09:00':
                channel = self.bot.get_channel(1031555995954057317)
                await channel.send(embed=embed,file=file)

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return

        if message.content.lower() in ['ゲソ', 'げそ', 'ゲソタウン', 'げそたうん', 'geso', 'gesotown']:
            #await ctx.defer()
            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["pickupBrand"]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["pickupBrand"]["brandGears"][0]["gear"]["name"]
            bgearpower = jsonData["pickupBrand"]["brandGears"][0]["gear"]["primaryGearPower"]
            bprice = jsonData["pickupBrand"]["brandGears"][0]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["pickupBrand"]["brandGears"][0]["gear"]["image"]["url"]

            embed = discord.Embed(
                                        title = "ブランドピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}￥**")
            embed.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            embed.set_thumbnail(url=bimage)

            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["pickupBrand"]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["pickupBrand"]["brandGears"][1]["gear"]["name"]
            bgearpower = jsonData["pickupBrand"]["brandGears"][1]["gear"]["primaryGearPower"]
            bprice = jsonData["pickupBrand"]["brandGears"][1]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["pickupBrand"]["brandGears"][1]["gear"]["image"]["url"]

            embed2 = discord.Embed(
                                        title = "ブランドピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}￥**")
            embed2.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            embed2.set_thumbnail(url=bimage)

            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["pickupBrand"]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["pickupBrand"]["brandGears"][2]["gear"]["name"]
            bgearpower = jsonData["pickupBrand"]["brandGears"][2]["gear"]["primaryGearPower"]
            bprice = jsonData["pickupBrand"]["brandGears"][2]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["pickupBrand"]["brandGears"][2]["gear"]["image"]["url"]

            embed3 = discord.Embed(
                                        title = "ブランドピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}**￥")
            embed3.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            embed3.set_thumbnail(url=bimage)

            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["limitedGears"][0]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["limitedGears"][0]["gear"]["name"]
            bgearpower = jsonData["limitedGears"][0]["gear"]["primaryGearPower"]
            bprice = jsonData["limitedGears"][0]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["limitedGears"][0]["gear"]["image"]["url"]

            embed4 = discord.Embed(
                                        title = "ピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}**￥")
            embed4.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            embed4.set_thumbnail(url=bimage)

            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["limitedGears"][1]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["limitedGears"][1]["gear"]["name"]
            bgearpower = jsonData["limitedGears"][1]["gear"]["primaryGearPower"]
            bprice = jsonData["limitedGears"][1]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["limitedGears"][1]["gear"]["image"]["url"]

            embed5 = discord.Embed(
                                        title = "ピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}**￥")
            embed5.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            embed5.set_thumbnail(url=bimage)

            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["limitedGears"][2]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["limitedGears"][2]["gear"]["name"]
            bgearpower = jsonData["limitedGears"][2]["gear"]["primaryGearPower"]
            bprice = jsonData["limitedGears"][2]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["limitedGears"][2]["gear"]["image"]["url"]

            embed6 = discord.Embed(
                                        title = "ピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}**￥")
            embed6.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            embed6.set_thumbnail(url=bimage)

            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["limitedGears"][3]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["limitedGears"][3]["gear"]["name"]
            bgearpower = jsonData["limitedGears"][3]["gear"]["primaryGearPower"]
            bprice = jsonData["limitedGears"][3]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["limitedGears"][3]["gear"]["image"]["url"]

            embed7 = discord.Embed(
                                        title = "ピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}**￥")
            embed7.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            embed7.set_thumbnail(url=bimage)

            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["limitedGears"][4]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["limitedGears"][4]["gear"]["name"]
            bgearpower = jsonData["limitedGears"][4]["gear"]["primaryGearPower"]
            bprice = jsonData["limitedGears"][4]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["limitedGears"][4]["gear"]["image"]["url"]

            embed8 = discord.Embed(
                                        title = "ピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}**￥")
            embed8.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            embed8.set_thumbnail(url=bimage)

            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["limitedGears"][5]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["limitedGears"][5]["gear"]["name"]
            bgearpower = jsonData["limitedGears"][5]["gear"]["primaryGearPower"]
            bprice = jsonData["limitedGears"][5]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["limitedGears"][5]["gear"]["image"]["url"]

            embed9 = discord.Embed(
                                        title = "ピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}**￥")
            embed9.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            embed9.set_thumbnail(url=bimage)
            ctx = await self.bot.get_context(message)

            page = [embed,embed2,embed3,embed4,embed5,embed6,embed7,embed8,embed9]
            paginator = pages.Paginator(pages=page)
            paginator.add_button(pages.PaginatorButton(
                "first", label="<<", style=discord.ButtonStyle.primary))
            paginator.add_button(pages.PaginatorButton(
                "prev", label="<", style=discord.ButtonStyle.primary))
            paginator.add_button(pages.PaginatorButton(
                "page_indicator", style=discord.ButtonStyle.primary))
            paginator.add_button(pages.PaginatorButton(
                "next", label=">", style=discord.ButtonStyle.primary))
            paginator.add_button(pages.PaginatorButton(
                "last", label=">>", style=discord.ButtonStyle.primary))
            await paginator.send(ctx)           

    @slash_command(name='geso一覧',guild_ids=guild_ids, description='ゲソタウン情報を取得します。')
    async def gear(self, ctx: discord.ApplicationContext):
            await ctx.defer()
            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["pickupBrand"]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["pickupBrand"]["brandGears"][0]["gear"]["name"]
            bgearpower = jsonData["pickupBrand"]["brandGears"][0]["gear"]["primaryGearPower"]
            bprice = jsonData["pickupBrand"]["brandGears"][0]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["pickupBrand"]["brandGears"][0]["gear"]["image"]["url"]

            embed = discord.Embed(
                                        title = "ブランドピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}￥**")
            embed.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            embed.set_thumbnail(url=bimage)

            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["pickupBrand"]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["pickupBrand"]["brandGears"][1]["gear"]["name"]
            bgearpower = jsonData["pickupBrand"]["brandGears"][1]["gear"]["primaryGearPower"]
            bprice = jsonData["pickupBrand"]["brandGears"][1]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["pickupBrand"]["brandGears"][1]["gear"]["image"]["url"]

            embed2 = discord.Embed(
                                        title = "ブランドピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}￥**")
            embed2.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            embed2.set_thumbnail(url=bimage)

            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["pickupBrand"]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["pickupBrand"]["brandGears"][2]["gear"]["name"]
            bgearpower = jsonData["pickupBrand"]["brandGears"][2]["gear"]["primaryGearPower"]
            bprice = jsonData["pickupBrand"]["brandGears"][2]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["pickupBrand"]["brandGears"][2]["gear"]["image"]["url"]

            embed3 = discord.Embed(
                                        title = "ブランドピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}**￥")
            embed3.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            embed3.set_thumbnail(url=bimage)

            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["limitedGears"][0]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["limitedGears"][0]["gear"]["name"]
            bgearpower = jsonData["limitedGears"][0]["gear"]["primaryGearPower"]
            bprice = jsonData["limitedGears"][0]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["limitedGears"][0]["gear"]["image"]["url"]

            embed4 = discord.Embed(
                                        title = "ピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}**￥")
            embed4.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            embed4.set_thumbnail(url=bimage)

            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["limitedGears"][1]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["limitedGears"][1]["gear"]["name"]
            bgearpower = jsonData["limitedGears"][1]["gear"]["primaryGearPower"]
            bprice = jsonData["limitedGears"][1]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["limitedGears"][1]["gear"]["image"]["url"]

            embed5 = discord.Embed(
                                        title = "ピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}**￥")
            embed5.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            embed5.set_thumbnail(url=bimage)

            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["limitedGears"][2]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["limitedGears"][2]["gear"]["name"]
            bgearpower = jsonData["limitedGears"][2]["gear"]["primaryGearPower"]
            bprice = jsonData["limitedGears"][2]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["limitedGears"][2]["gear"]["image"]["url"]

            embed6 = discord.Embed(
                                        title = "ピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}**￥")
            embed6.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            embed6.set_thumbnail(url=bimage)

            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["limitedGears"][3]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["limitedGears"][3]["gear"]["name"]
            bgearpower = jsonData["limitedGears"][3]["gear"]["primaryGearPower"]
            bprice = jsonData["limitedGears"][3]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["limitedGears"][3]["gear"]["image"]["url"]

            embed7 = discord.Embed(
                                        title = "ピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}**￥")
            embed7.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            embed7.set_thumbnail(url=bimage)

            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["limitedGears"][4]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["limitedGears"][4]["gear"]["name"]
            bgearpower = jsonData["limitedGears"][4]["gear"]["primaryGearPower"]
            bprice = jsonData["limitedGears"][4]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["limitedGears"][4]["gear"]["image"]["url"]

            embed8 = discord.Embed(
                                        title = "ピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}**￥")
            embed8.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            embed8.set_thumbnail(url=bimage)

            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["limitedGears"][5]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["limitedGears"][5]["gear"]["name"]
            bgearpower = jsonData["limitedGears"][5]["gear"]["primaryGearPower"]
            bprice = jsonData["limitedGears"][5]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["limitedGears"][5]["gear"]["image"]["url"]

            embed9 = discord.Embed(
                                        title = "ピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}**￥")
            embed9.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            embed9.set_thumbnail(url=bimage)

            page = [embed,embed2,embed3,embed4,embed5,embed6,embed7,embed8,embed9]
            paginator = pages.Paginator(pages=page)
            paginator.add_button(pages.PaginatorButton(
                "first", label="<<", style=discord.ButtonStyle.primary))
            paginator.add_button(pages.PaginatorButton(
                "prev", label="<", style=discord.ButtonStyle.primary))
            paginator.add_button(pages.PaginatorButton(
                "page_indicator", style=discord.ButtonStyle.primary))
            paginator.add_button(pages.PaginatorButton(
                "next", label=">", style=discord.ButtonStyle.primary))
            paginator.add_button(pages.PaginatorButton(
                "last", label=">>", style=discord.ButtonStyle.primary))
            await paginator.respond(ctx.interaction, ephemeral=True)           

def setup(bot):
    bot.add_cog(gear3(bot))