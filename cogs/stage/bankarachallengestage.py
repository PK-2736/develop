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

print("bankarachallengestageの読み込み完了")

class bankarachallenge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.loop.start()

    @tasks.loop(seconds=60)
    async def loop(self):
            url = "https://spla3.yuu26.com/api/bankara-challenge/schedule"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            rule = jsonData["results"][0]["rule"]["name"]
            map = jsonData["results"][0]["stages"][0]["name"]
            map2 = jsonData["results"][0]["stages"][1]["name"]
            time = jsonData["results"][0]["start_time"]
            time2 = jsonData["results"][0]["end_time"]
            t = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
            n = t.strftime('%H:%M')
            t2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S%z')
            n2 = t2.strftime('%H:%M') 

            rule2 = jsonData["results"][1]["rule"]["name"]
            map3 = jsonData["results"][1]["stages"][0]["name"]
            map4 = jsonData["results"][1]["stages"][1]["name"]
            time3 = jsonData["results"][1]["start_time"]
            time4 = jsonData["results"][1]["end_time"]
            t3 = datetime.strptime(time3, '%Y-%m-%dT%H:%M:%S%z')
            n3 = t3.strftime('%H:%M')
            t4 = datetime.strptime(time4, '%Y-%m-%dT%H:%M:%S%z')
            n4 = t4.strftime('%H:%M')   

            rule3 = jsonData["results"][2]["rule"]["name"]
            map5 = jsonData["results"][2]["stages"][0]["name"]
            map6 = jsonData["results"][2]["stages"][1]["name"]
            time5 = jsonData["results"][2]["start_time"]
            time6 = jsonData["results"][2]["end_time"]
            t5 = datetime.strptime(time5, '%Y-%m-%dT%H:%M:%S%z')
            n5 = t5.strftime('%H:%M')
            t6 = datetime.strptime(time6, '%Y-%m-%dT%H:%M:%S%z')
            n6 = t6.strftime('%H:%M')         

            rule4 = jsonData["results"][3]["rule"]["name"]
            map7 = jsonData["results"][3]["stages"][0]["name"]
            map8 = jsonData["results"][3]["stages"][1]["name"]
            time7 = jsonData["results"][3]["start_time"]
            time8 = jsonData["results"][3]["end_time"]
            t7 = datetime.strptime(time7, '%Y-%m-%dT%H:%M:%S%z')
            n7 = t7.strftime('%H:%M')
            t8 = datetime.strptime(time8, '%Y-%m-%dT%H:%M:%S%z')
            n8 = t8.strftime('%H:%M') 

            rule5 = jsonData["results"][4]["rule"]["name"]
            map9 = jsonData["results"][4]["stages"][0]["name"]
            map10 = jsonData["results"][4]["stages"][1]["name"]
            time9 = jsonData["results"][4]["start_time"]
            time10 = jsonData["results"][4]["end_time"]
            t9 = datetime.strptime(time9, '%Y-%m-%dT%H:%M:%S%z')
            n9 = t9.strftime('%H:%M')
            t10 = datetime.strptime(time10, '%Y-%m-%dT%H:%M:%S%z')
            n10 = t10.strftime('%H:%M')

            rule6 = jsonData["results"][5]["rule"]["name"]
            map11 = jsonData["results"][5]["stages"][0]["name"]
            map12 = jsonData["results"][5]["stages"][1]["name"]
            time11 = jsonData["results"][5]["start_time"]
            time12 = jsonData["results"][5]["end_time"]
            t11 = datetime.strptime(time11, '%Y-%m-%dT%H:%M:%S%z')
            n11 = t11.strftime('%H:%M')
            t12 = datetime.strptime(time12, '%Y-%m-%dT%H:%M:%S%z')
            n12 = t12.strftime('%H:%M')

            # rule7 = jsonData["results"][6]["rule"]["name"]
            # map13 = jsonData["results"][6]["stages"][0]["name"]
            # map14 = jsonData["results"][6]["stages"][1]["name"]
            # time13 = jsonData["results"][6]["start_time"]
            # time14 = jsonData["results"][6]["end_time"]
            # t13 = datetime.strptime(time13, '%Y-%m-%dT%H:%M:%S%z')
            # n13 = t13.strftime('%H:%M')
            # t14 = datetime.strptime(time14, '%Y-%m-%dT%H:%M:%S%z')
            # n14 = t14.strftime('%H:%M')

            # rule8 = jsonData["results"][7]["rule"]["name"]
            # map15 = jsonData["results"][7]["stages"][0]["name"]
            # map16 = jsonData["results"][7]["stages"][1]["name"]
            # time15 = jsonData["results"][7]["start_time"]
            # time16 = jsonData["results"][7]["end_time"]
            # t15 = datetime.strptime(time15, '%Y-%m-%dT%H:%M:%S%z')
            # n15 = t15.strftime('%H:%M')
            # t16 = datetime.strptime(time16, '%Y-%m-%dT%H:%M:%S%z')
            # n16 = t16.strftime('%H:%M')

            # rule9 = jsonData["results"][8]["rule"]["name"]
            # map17 = jsonData["results"][8]["stages"][0]["name"]
            # map18 = jsonData["results"][8]["stages"][1]["name"]
            # time17 = jsonData["results"][8]["start_time"]
            # time18 = jsonData["results"][8]["end_time"]
            # t17 = datetime.strptime(time17, '%Y-%m-%dT%H:%M:%S%z')
            # n17 = t17.strftime('%H:%M')
            # t18 = datetime.strptime(time18, '%Y-%m-%dT%H:%M:%S%z')
            # n18 = t18.strftime('%H:%M')

            # rule10 = jsonData["results"][9]["rule"]["name"]
            # map19 = jsonData["results"][9]["stages"][0]["name"]
            # map20 = jsonData["results"][9]["stages"][1]["name"]
            # time19 = jsonData["results"][9]["start_time"]
            # time20 = jsonData["results"][9]["end_time"]
            # t19 = datetime.strptime(time19, '%Y-%m-%dT%H:%M:%S%z')
            # n19 = t19.strftime('%H:%M')
            # t20 = datetime.strptime(time20, '%Y-%m-%dT%H:%M:%S%z')
            # n20 = t20.strftime('%H:%M')

            # rule11 = jsonData["results"][10]["rule"]["name"]
            # map21 = jsonData["results"][10]["stages"][0]["name"]
            # map22 = jsonData["results"][10]["stages"][1]["name"]
            # time21 = jsonData["results"][10]["start_time"]
            # time22 = jsonData["results"][10]["end_time"]
            # t21 = datetime.strptime(time21, '%Y-%m-%dT%H:%M:%S%z')
            # n21 = t21.strftime('%H:%M')
            # t22 = datetime.strptime(time22, '%Y-%m-%dT%H:%M:%S%z')
            # n22 = t22.strftime('%H:%M')

            # rule12 = jsonData["results"][11]["rule"]["name"]
            # map23 = jsonData["results"][11]["stages"][0]["name"]
            # map24 = jsonData["results"][11]["stages"][1]["name"]
            # time23 = jsonData["results"][11]["start_time"]
            # time24 = jsonData["results"][11]["end_time"]
            # t23 = datetime.strptime(time23, '%Y-%m-%dT%H:%M:%S%z')
            # n23 = t23.strftime('%H:%M')
            # t24 = datetime.strptime(time24, '%Y-%m-%dT%H:%M:%S%z')
            # n24 = t24.strftime('%H:%M')

            embed = discord.Embed(title='バンカラチャレンジ',color=0xdb4a13,
                                 description=f"**{n}～{n2} [{rule}]**\n**{map}/{map2}**\n\n"
                                 f"**{n3}～{n4} [{rule2}]**\n**{map3}/{map4}**\n\n"
                                 f"**{n5}～{n6} [{rule3}]**\n**{map5}/{map6}**\n\n"
                                 f"**{n7}～{n8} [{rule4}]**\n**{map7}/{map8}**\n\n"
                                 f"**{n9}～{n10} [{rule5}]**\n**{map9}/{map10}**\n\n"
                                 f"**{n11}～{n12} [{rule6}]**\n**{map11}/{map12}**\n\n")
                                #  f"**{n13}～{n14} [{rule7}]**\n**{map13}/{map14}**\n\n"
                                #  f"**{n15}～{n16} [{rule8}]**\n**{map15}/{map16}**\n\n"
                                #  f"**{n17}～{n18} [{rule9}]**\n**{map17}/{map18}**\n\n"
                                #  f"**{n19}～{n20} [{rule10}]**\n**{map19}/{map20}**\n\n"
                                #  f"**{n21}～{n22} [{rule11}]**\n**{map21}/{map22}**\n\n"
                                #  f"**{n23}～{n24} [{rule12}]**\n**{map23}/{map24}**\n\n")

            embed.set_thumbnail(url="http://cocohp.com/students/free2019/010/images/bt04.png")
            embed.set_footer(text="API: https://spla3.yuu26.com| イカコード3")
            now = datetime.now().strftime('%H:%M')
            if now == '09:00' or now == '21:00':
                channel = self.bot.get_channel(1031555349876051968)
                await channel.send(embed=embed)  

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return

        if message.content.lower() in ['バンカラチャレンジ', 'ばんからちゃれんじ', 'challenge', 'bankarachallenge', 'チャレンジ', 'ちゃれんじ']:
            url = "https://spla3.yuu26.com/api/bankara-challenge/schedule"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            rule = jsonData["results"][0]["rule"]["name"]
            map = jsonData["results"][0]["stages"][0]["name"]
            map2 = jsonData["results"][0]["stages"][1]["name"]
            time = jsonData["results"][0]["start_time"]
            time2 = jsonData["results"][0]["end_time"]
            t = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
            n = t.strftime('%H:%M')
            t2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S%z')
            n2 = t2.strftime('%H:%M')
            image = jsonData["results"][0]["stages"][0]["image"]
            image2 = jsonData["results"][0]["stages"][1]["image"]

            img = Image.new('RGB', (800,200), (0, 0, 0))
            im1 = Image.open(io.BytesIO(requests.get(image).content))
            im2 = Image.open(io.BytesIO(requests.get(image2).content))
            img_binary = io.BytesIO()
            img.paste(im1, (405,0))
            img.paste(im2, (0,0))
            img.save(img_binary, format='PNG')
            img_binary.seek(0)

            embed = discord.Embed(
                                        title = "バンカラチャレンジ",
                                        color=0xdb4a13,

                                        description=f"**{n}から{n2}まで**\n\n**{rule}**\n\n**{map}**\n**{map2}**")
            file = discord.File(img_binary, filename='image.png')
            embed.set_image(url="attachment://image.png")
            embed.set_thumbnail(url="http://cocohp.com/students/free2019/010/images/bt04.png")
            embed.set_footer(text="API: https://spla3.yuu26.com| イカコード3")
            ctx = await self.bot.get_context(message)

            await ctx.send(embed=embed,file=file)

        if message.content.lower() in ['次のバンカラチャレンジ', 'つぎのばんからちゃれんじ', 'nextchallenge', 'nextbankarachallenge', '次のチャレンジ', 'つぎのちゃれんじ']:
            url1 = "https://spla3.yuu26.com/api/bankara-challenge/schedule"
            response = requests.get(url1)
            jsonData = response.json()
            rule = jsonData["results"][1]["rule"]["name"]
            map = jsonData["results"][1]["stages"][0]["name"]
            map2 = jsonData["results"][1]["stages"][1]["name"]
            time = jsonData["results"][1]["start_time"]
            time2 = jsonData["results"][1]["end_time"]
            t = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
            n = t.strftime('%H:%M')
            t2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S%z')
            n2 = t2.strftime('%H:%M')
            image = jsonData["results"][1]["stages"][0]["image"]
            image2 = jsonData["results"][1]["stages"][1]["image"]

            img1 = Image.new('RGB', (800,200), (0, 0, 0))
            im3 = Image.open(io.BytesIO(requests.get(image).content))
            im4 = Image.open(io.BytesIO(requests.get(image2).content))
            img_binary1 = io.BytesIO()
            img1.paste(im3, (405,0))
            img1.paste(im4, (0,0))
            img1.save(img_binary1, format='PNG')
            img_binary1.seek(0)
            embed2 = discord.Embed(
                                        title = "バンカラチャレンジ",
                                        color=0xdb4a13,

                                        description=f"**{n}から{n2}まで**\n\n**{rule}**\n\n**{map}**\n**{map2}**")
            file1 = discord.File(img_binary1, filename='image1.png')
            embed2.set_image(url="attachment://image1.png")
            embed2.set_thumbnail(url="http://cocohp.com/students/free2019/010/images/bt04.png")
            embed2.set_footer(text="API: https://spla3.yuu26.com| イカコード3")
            ctx = await self.bot.get_context(message)

            await ctx.send(embed=embed2,file=file1)

        if message.content.lower() in ['次の次のバンカラチャレンジ', 'つぎのつぎのばんからちゃれんじ', 'afternextchallenge', 'afternextbankarachallenge', '次の次のチャレンジ', 'つぎのつぎのちゃれんじ']:
            url1 = "https://spla3.yuu26.com/api/bankara-challenge/schedule"
            response = requests.get(url1)
            jsonData = response.json()
            rule = jsonData["results"][2]["rule"]["name"]
            map = jsonData["results"][2]["stages"][0]["name"]
            map2 = jsonData["results"][2]["stages"][1]["name"]
            time = jsonData["results"][2]["start_time"]
            time2 = jsonData["results"][2]["end_time"]
            t = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
            n = t.strftime('%H:%M')
            t2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S%z')
            n2 = t2.strftime('%H:%M')
            image = jsonData["results"][2]["stages"][0]["image"]
            image2 = jsonData["results"][2]["stages"][1]["image"]

            img2 = Image.new('RGB', (800,200), (0, 0, 0))
            im5 = Image.open(io.BytesIO(requests.get(image).content))
            im6 = Image.open(io.BytesIO(requests.get(image2).content))
            img_binary2 = io.BytesIO()
            img2.paste(im5, (405,0))
            img2.paste(im6, (0,0))
            img2.save(img_binary2, format='PNG')
            img_binary2.seek(0)
            embed3 = discord.Embed(
                                        title = "バンカラチャレンジ",
                                        color=0xdb4a13,

                                        description=f"**{n}から{n2}まで**\n\n**{rule}**\n\n**{map}**\n**{map2}**")
            file2 = discord.File(img_binary2, filename='image2.png')
            embed3.set_image(url="attachment://image2.png")
            embed3.set_thumbnail(url="http://cocohp.com/students/free2019/010/images/bt04.png")
            embed3.set_footer(text="API: https://spla3.yuu26.com| イカコード3")
            ctx = await self.bot.get_context(message)

            await ctx.send(embed=embed3,file=file2)
    
    @slash_command(name='すてチャレンジ', guild_ids = guild_ids, description='バンカラチャレンジのステージ情報を取得します。')
    async def bankarachallenge(self, ctx, time : Option(str, '時間', choices=["今", "次", "次の次"])):
        await ctx.defer()

        if time == "今":
            url = "https://spla3.yuu26.com/api/bankara-challenge/schedule"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            rule = jsonData["results"][0]["rule"]["name"]
            map = jsonData["results"][0]["stages"][0]["name"]
            map2 = jsonData["results"][0]["stages"][1]["name"]
            time = jsonData["results"][0]["start_time"]
            time2 = jsonData["results"][0]["end_time"]
            t = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
            n = t.strftime('%H:%M')
            t2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S%z')
            n2 = t2.strftime('%H:%M')
            image = jsonData["results"][0]["stages"][0]["image"]
            image2 = jsonData["results"][0]["stages"][1]["image"]

            img = Image.new('RGB', (800,200), (0, 0, 0))
            im1 = Image.open(io.BytesIO(requests.get(image).content))
            im2 = Image.open(io.BytesIO(requests.get(image2).content))
            img_binary = io.BytesIO()
            img.paste(im1, (405,0))
            img.paste(im2, (0,0))
            img.save(img_binary, format='PNG')
            img_binary.seek(0)

            embed = discord.Embed(
                                        title = "バンカラチャレンジ",
                                        color=0xdb4a13,

                                        description=f"**{n}から{n2}まで**\n\n**{rule}**\n\n**{map}**\n**{map2}**")
            file = discord.File(img_binary, filename='image.png')
            embed.set_image(url="attachment://image.png")
            embed.set_thumbnail(url="http://cocohp.com/students/free2019/010/images/bt04.png")
            embed.set_footer(text="API: https://spla3.yuu26.com| イカコード3")

            await ctx.respond(embed=embed,file=file,ephemeral = True)

        if time == "次":
            url1 = "https://spla3.yuu26.com/api/bankara-challenge/schedule"
            response = requests.get(url1)
            jsonData = response.json()
            rule = jsonData["results"][1]["rule"]["name"]
            map = jsonData["results"][1]["stages"][0]["name"]
            map2 = jsonData["results"][1]["stages"][1]["name"]
            time = jsonData["results"][1]["start_time"]
            time2 = jsonData["results"][1]["end_time"]
            t = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
            n = t.strftime('%H:%M')
            t2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S%z')
            n2 = t2.strftime('%H:%M')
            image = jsonData["results"][1]["stages"][0]["image"]
            image2 = jsonData["results"][1]["stages"][1]["image"]

            img1 = Image.new('RGB', (800,200), (0, 0, 0))
            im3 = Image.open(io.BytesIO(requests.get(image).content))
            im4 = Image.open(io.BytesIO(requests.get(image2).content))
            img_binary1 = io.BytesIO()
            img1.paste(im3, (405,0))
            img1.paste(im4, (0,0))
            img1.save(img_binary1, format='PNG')
            img_binary1.seek(0)
            embed2 = discord.Embed(
                                        title = "バンカラチャレンジ",
                                        color=0xdb4a13,

                                        description=f"**{n}から{n2}まで**\n\n**{rule}**\n\n**{map}**\n**{map2}**")
            file1 = discord.File(img_binary1, filename='image1.png')
            embed2.set_image(url="attachment://image1.png")
            embed2.set_thumbnail(url="http://cocohp.com/students/free2019/010/images/bt04.png")
            embed2.set_footer(text="API: https://spla3.yuu26.com| イカコード3")
    
            await ctx.respond(embed=embed2,file=file1,ephemeral = True)

        if time == "次の次":
            url1 = "https://spla3.yuu26.com/api/bankara-challenge/schedule"
            response = requests.get(url1)
            jsonData = response.json()
            rule = jsonData["results"][2]["rule"]["name"]
            map = jsonData["results"][2]["stages"][0]["name"]
            map2 = jsonData["results"][2]["stages"][1]["name"]
            time = jsonData["results"][2]["start_time"]
            time2 = jsonData["results"][2]["end_time"]
            t = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
            n = t.strftime('%H:%M')
            t2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S%z')
            n2 = t2.strftime('%H:%M')
            image = jsonData["results"][2]["stages"][0]["image"]
            image2 = jsonData["results"][2]["stages"][1]["image"]

            img2 = Image.new('RGB', (800,200), (0, 0, 0))
            im5 = Image.open(io.BytesIO(requests.get(image).content))
            im6 = Image.open(io.BytesIO(requests.get(image2).content))
            img_binary2 = io.BytesIO()
            img2.paste(im5, (405,0))
            img2.paste(im6, (0,0))
            img2.save(img_binary2, format='PNG')
            img_binary2.seek(0)
            embed3 = discord.Embed(
                                        title = "バンカラチャレンジ",
                                        color=0xdb4a13,

                                        description=f"**{n}から{n2}まで**\n\n**{rule}**\n\n**{map}**\n**{map2}**")
            file2 = discord.File(img_binary2, filename='image2.png')
            embed3.set_image(url="attachment://image2.png")
            embed3.set_thumbnail(url="http://cocohp.com/students/free2019/010/images/bt04.png")
            embed3.set_footer(text="API: https://spla3.yuu26.com| イカコード3")
    
            await ctx.respond(embed=embed3,file=file2,ephemeral = True)


def setup(bot):
    bot.add_cog(bankarachallenge(bot))