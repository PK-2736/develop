from discord.ext import commands
import discord
from discord.commands import slash_command, Option
from datetime import datetime
import requests
from discord.ext import pages
from cogs import guild_ids

print("gesocmdの読み込み完了")

class cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='ゲソタウン',guild_ids=guild_ids, description='ゲソタウン情報を取得します。')
    async def gear(self, ctx: discord.ApplicationContext):
        await ctx.defer()

        url = "https://splatoon3.ink/data/gear.json"
        response = requests.get(url)
        jsonData = response.json()
        image = jsonData["data"]["gesotown"]["pickupBrand"]["brandGears"][0]["gear"]["image"]["url"]

        url2 = "https://api.koukun.jp/splatoon/3/geso/"
        ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
        headers = {"User-Agent": ua}
        response = requests.get(url2)
        jsonData = response.json()
        btime = jsonData["pickupBrand"]["saleEndTime"]
        t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
        n = t.strftime('%m/%d %H:%M')
        gear = jsonData["pickupBrand"]["brandGears"][0]["gear"]["name"]
        brand = jsonData["pickupBrand"]["brandGears"][0]["gear"]["brand"]["name"]
        bgearpower = jsonData["pickupBrand"]["brandGears"][0]["gear"]["primaryGearPower"]
        price = jsonData["pickupBrand"]["brandGears"][0]["price"]

        henkan = (bgearpower
                       .replace('ラストスパート', '<:gp1:1035875883493380196>')
                       .replace('イカニンジャ', '<:gp2:1035875858197512223>')
                       .replace('インク効率アップ(メイン)', '<:gp3:1035875881991811084>')
                       .replace('スペシャル減少量ダウン', '<:gp4:1035875877059297290>')
                       .replace('スタートダッシュ', '<:gp5:1035875870189047878>')
                       .replace('カムバック', '<:gp6:1035875861670395904>')
                       .replace('復活ペナルティアップ', '<:gp7:1035875889793224707>')
                       .replace('サブ性能アップ', '<:gp8:1035875866569347207>')
                       .replace('対物攻撃力アップ', '<:gp9:1035875888526532698>')
                       .replace('逆境強化', '<:gp10:1035875898030833684>')
                       .replace('リベンジ', '<:gp11:1035875884919439460>')
                       .replace('スーパージャンプ時間短縮', '<:gp12:1035875878854475846>')
                       .replace('インク回復力アップ', '<:gp13:1035875859631972383>')
                       .replace('相手インク影響軽減', '<:gp14:1035875894390161428>')
                       .replace('ステルスジャンプ', '<:gp15:1035875872055513088>')
                       .replace('受け身術', '<:gp16:1035875886798479370>')
                       .replace('サーマルインク', '<:gp17:1035875868431626291>')
                       .replace('追加ギアパワー倍化', '<:gp18:1035875896193732608>')
                       .replace('インク効率アップ(サブ)', '<:gp19:1035875863566221403>')
                       .replace('ヒト移動速度アップ', '<:gp20:1035875880507031562>')
                       .replace('スペシャル性能アップ', '<:gp21:1035875875448700928>')
                       .replace('イカダッシュ速度アップ', '<:gp22:1035875856553361438>')
                       .replace('スペシャル増加量アップ', '<:gp23:1035875873741619241>')
                       .replace('復活時間短縮', '<:gp24:1035875892775370752>')
                       .replace('アクション強化', '<:gp25:1035875854921764964>')
                       .replace('サブ影響軽減', '<:gp26:1035875865319456858>')
                       )
        hatena = '<:gp27:1035875901130416218>'
        okane = '<:cash:1035875899637248110>'
        try:
            jsonData["pickupBrand"]["brandGears"][0]["gear"]["additionalGearPowers"][1]["name"]
        except IndexError:
            embed1 = discord.Embed(
                        title = "ピックアップ",
                        color=0x457fce,
                        description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")
            embed1.add_field(name="ギアパワー", value=f"{henkan}|{hatena}", inline=True)
            embed1.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
            embed1.set_thumbnail(url=image)
            embed1.set_footer(text="API: https://splatoon3.ink/| イカコード3")
        else:
            embed1 = discord.Embed(
                        title = "ピックアップ",
                        color=0x457fce,
                        description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")  
            embed1.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}", inline=True)
            embed1.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
            embed1.set_thumbnail(url=image)
            embed1.set_footer(text="API: https://splatoon3.ink/| イカコード3")

            try:
                jsonData["pickupBrand"]["brandGears"][0]["gear"]["additionalGearPowers"][2]["name"]
            except IndexError:    
                embed1 = discord.Embed(
                            title = "ピックアップ",
                            color=0x457fce,
                            description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n") 
                embed1.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}", inline=True)
                embed1.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
                embed1.set_thumbnail(url=image)
                embed1.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            else:
                embed1 = discord.Embed(
                            title = "ピックアップ",
                            color=0x457fce,
                            description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")  
                embed1.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}{hatena}", inline=True)
                embed1.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
                embed1.set_thumbnail(url=image)
                embed1.set_footer(text="API: https://splatoon3.ink/| イカコード3")

        url = "https://splatoon3.ink/data/gear.json"
        response = requests.get(url)
        jsonData = response.json()
        image = jsonData["data"]["gesotown"]["pickupBrand"]["brandGears"][1]["gear"]["image"]["url"]

        url2 = "https://api.koukun.jp/splatoon/3/geso/"
        ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
        headers = {"User-Agent": ua}
        response = requests.get(url2)
        jsonData = response.json()
        btime = jsonData["pickupBrand"]["saleEndTime"]
        t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
        n = t.strftime('%m/%d %H:%M')
        gear = jsonData["pickupBrand"]["brandGears"][1]["gear"]["name"]
        brand = jsonData["pickupBrand"]["brandGears"][1]["gear"]["brand"]["name"]
        bgearpower = jsonData["pickupBrand"]["brandGears"][1]["gear"]["primaryGearPower"]
        price = jsonData["pickupBrand"]["brandGears"][1]["price"]

        henkan = (bgearpower
                       .replace('ラストスパート', '<:gp1:1035875883493380196>')
                       .replace('イカニンジャ', '<:gp2:1035875858197512223>')
                       .replace('インク効率アップ(メイン)', '<:gp3:1035875881991811084>')
                       .replace('スペシャル減少量ダウン', '<:gp4:1035875877059297290>')
                       .replace('スタートダッシュ', '<:gp5:1035875870189047878>')
                       .replace('カムバック', '<:gp6:1035875861670395904>')
                       .replace('復活ペナルティアップ', '<:gp7:1035875889793224707>')
                       .replace('サブ性能アップ', '<:gp8:1035875866569347207>')
                       .replace('対物攻撃力アップ', '<:gp9:1035875888526532698>')
                       .replace('逆境強化', '<:gp10:1035875898030833684>')
                       .replace('リベンジ', '<:gp11:1035875884919439460>')
                       .replace('スーパージャンプ時間短縮', '<:gp12:1035875878854475846>')
                       .replace('インク回復力アップ', '<:gp13:1035875859631972383>')
                       .replace('相手インク影響軽減', '<:gp14:1035875894390161428>')
                       .replace('ステルスジャンプ', '<:gp15:1035875872055513088>')
                       .replace('受け身術', '<:gp16:1035875886798479370>')
                       .replace('サーマルインク', '<:gp17:1035875868431626291>')
                       .replace('追加ギアパワー倍化', '<:gp18:1035875896193732608>')
                       .replace('インク効率アップ(サブ)', '<:gp19:1035875863566221403>')
                       .replace('ヒト移動速度アップ', '<:gp20:1035875880507031562>')
                       .replace('スペシャル性能アップ', '<:gp21:1035875875448700928>')
                       .replace('イカダッシュ速度アップ', '<:gp22:1035875856553361438>')
                       .replace('スペシャル増加量アップ', '<:gp23:1035875873741619241>')
                       .replace('復活時間短縮', '<:gp24:1035875892775370752>')
                       .replace('アクション強化', '<:gp25:1035875854921764964>')
                       .replace('サブ影響軽減', '<:gp26:1035875865319456858>')
                       )
        try:
            jsonData["pickupBrand"]["brandGears"][1]["gear"]["additionalGearPowers"][1]["name"]
        except IndexError:
            embed2 = discord.Embed(
                        title = "ピックアップ",
                        color=0x457fce,
                        description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")
            embed2.add_field(name="ギアパワー", value=f"{henkan}|{hatena}", inline=True)
            embed2.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
            embed2.set_thumbnail(url=image)
            embed2.set_footer(text="API: https://splatoon3.ink/| イカコード3")
        else:
            embed2 = discord.Embed(
                        title = "ピックアップ",
                        color=0x457fce,
                        description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")  
            embed2.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}", inline=True)
            embed2.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
            embed2.set_thumbnail(url=image)
            embed2.set_footer(text="API: https://splatoon3.ink/| イカコード3")

            try:
                jsonData["pickupBrand"]["brandGears"][1]["gear"]["additionalGearPowers"][2]["name"]
            except IndexError:    
                embed2 = discord.Embed(
                            title = "ピックアップ",
                            color=0x457fce,
                            description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n") 
                embed2.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}", inline=True)
                embed2.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
                embed2.set_thumbnail(url=image)
                embed2.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            else:
                embed2 = discord.Embed(
                            title = "ピックアップ",
                            color=0x457fce,
                            description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")  
                embed2.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}{hatena}", inline=True)
                embed2.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
                embed2.set_thumbnail(url=image)
                embed2.set_footer(text="API: https://splatoon3.ink/| イカコード3")

        url = "https://splatoon3.ink/data/gear.json"
        response = requests.get(url)
        jsonData = response.json()
        image = jsonData["data"]["gesotown"]["pickupBrand"]["brandGears"][2]["gear"]["image"]["url"]

        url2 = "https://api.koukun.jp/splatoon/3/geso/"
        ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
        headers = {"User-Agent": ua}
        response = requests.get(url2)
        jsonData = response.json()
        btime = jsonData["pickupBrand"]["saleEndTime"]
        t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
        n = t.strftime('%m/%d %H:%M')
        gear = jsonData["pickupBrand"]["brandGears"][2]["gear"]["name"]
        brand = jsonData["pickupBrand"]["brandGears"][2]["gear"]["brand"]["name"]
        bgearpower = jsonData["pickupBrand"]["brandGears"][2]["gear"]["primaryGearPower"]
        price = jsonData["pickupBrand"]["brandGears"][2]["price"]

        henkan = (bgearpower
                       .replace('ラストスパート', '<:gp1:1035875883493380196>')
                       .replace('イカニンジャ', '<:gp2:1035875858197512223>')
                       .replace('インク効率アップ(メイン)', '<:gp3:1035875881991811084>')
                       .replace('スペシャル減少量ダウン', '<:gp4:1035875877059297290>')
                       .replace('スタートダッシュ', '<:gp5:1035875870189047878>')
                       .replace('カムバック', '<:gp6:1035875861670395904>')
                       .replace('復活ペナルティアップ', '<:gp7:1035875889793224707>')
                       .replace('サブ性能アップ', '<:gp8:1035875866569347207>')
                       .replace('対物攻撃力アップ', '<:gp9:1035875888526532698>')
                       .replace('逆境強化', '<:gp10:1035875898030833684>')
                       .replace('リベンジ', '<:gp11:1035875884919439460>')
                       .replace('スーパージャンプ時間短縮', '<:gp12:1035875878854475846>')
                       .replace('インク回復力アップ', '<:gp13:1035875859631972383>')
                       .replace('相手インク影響軽減', '<:gp14:1035875894390161428>')
                       .replace('ステルスジャンプ', '<:gp15:1035875872055513088>')
                       .replace('受け身術', '<:gp16:1035875886798479370>')
                       .replace('サーマルインク', '<:gp17:1035875868431626291>')
                       .replace('追加ギアパワー倍化', '<:gp18:1035875896193732608>')
                       .replace('インク効率アップ(サブ)', '<:gp19:1035875863566221403>')
                       .replace('ヒト移動速度アップ', '<:gp20:1035875880507031562>')
                       .replace('スペシャル性能アップ', '<:gp21:1035875875448700928>')
                       .replace('イカダッシュ速度アップ', '<:gp22:1035875856553361438>')
                       .replace('スペシャル増加量アップ', '<:gp23:1035875873741619241>')
                       .replace('復活時間短縮', '<:gp24:1035875892775370752>')
                       .replace('アクション強化', '<:gp25:1035875854921764964>')
                       .replace('サブ影響軽減', '<:gp26:1035875865319456858>')
                       )
        try:
            jsonData["pickupBrand"]["brandGears"][2]["gear"]["additionalGearPowers"][1]["name"]
        except IndexError:
            embed3 = discord.Embed(
                        title = "ピックアップ",
                        color=0x457fce,
                        description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")
            embed3.add_field(name="ギアパワー", value=f"{henkan}|{hatena}", inline=True)
            embed3.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
            embed3.set_thumbnail(url=image)
            embed3.set_footer(text="API: https://splatoon3.ink/| イカコード3")
        else:
            embed3 = discord.Embed(
                        title = "ピックアップ",
                        color=0x457fce,
                        description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")  
            embed3.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}", inline=True)
            embed3.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
            embed3.set_thumbnail(url=image)
            embed3.set_footer(text="API: https://splatoon3.ink/| イカコード3")

            try:
                jsonData["pickupBrand"]["brandGears"][2]["gear"]["additionalGearPowers"][2]["name"]
            except IndexError:    
                embed3 = discord.Embed(
                            title = "ピックアップ",
                            color=0x457fce,
                            description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n") 
                embed3.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}", inline=True)
                embed3.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
                embed3.set_thumbnail(url=image)
                embed3.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            else:
                embed3 = discord.Embed(
                            title = "ピックアップ",
                            color=0x457fce,
                            description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")  
                embed3.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}{hatena}", inline=True)
                embed3.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
                embed3.set_thumbnail(url=image)
                embed3.set_footer(text="API: https://splatoon3.ink/| イカコード3")

        url = "https://splatoon3.ink/data/gear.json"
        response = requests.get(url)
        jsonData = response.json()
        image = jsonData["data"]["gesotown"]["limitedGears"][5]["gear"]["image"]["url"]

        url2 = "https://api.koukun.jp/splatoon/3/geso/"
        ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
        headers = {"User-Agent": ua}
        response = requests.get(url2)
        jsonData = response.json()
        time = jsonData["limitedGears"][5]["saleEndTime"]
        t = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        n = t.strftime('%m/%d %H:%M')
        gear = jsonData["limitedGears"][5]["gear"]["name"]
        brand = jsonData["limitedGears"][5]["gear"]["brand"]["name"]
        power1 = jsonData["limitedGears"][5]["gear"]["primaryGearPower"]
        price = jsonData["limitedGears"][5]["price"]

        henkan = (power1
                       .replace('ラストスパート', '<:gp1:1035875883493380196>')
                       .replace('イカニンジャ', '<:gp2:1035875858197512223>')
                       .replace('インク効率アップ(メイン)', '<:gp3:1035875881991811084>')
                       .replace('スペシャル減少量ダウン', '<:gp4:1035875877059297290>')
                       .replace('スタートダッシュ', '<:gp5:1035875870189047878>')
                       .replace('カムバック', '<:gp6:1035875861670395904>')
                       .replace('復活ペナルティアップ', '<:gp7:1035875889793224707>')
                       .replace('サブ性能アップ', '<:gp8:1035875866569347207>')
                       .replace('対物攻撃力アップ', '<:gp9:1035875888526532698>')
                       .replace('逆境強化', '<:gp10:1035875898030833684>')
                       .replace('リベンジ', '<:gp11:1035875884919439460>')
                       .replace('スーパージャンプ時間短縮', '<:gp12:1035875878854475846>')
                       .replace('インク回復力アップ', '<:gp13:1035875859631972383>')
                       .replace('相手インク影響軽減', '<:gp14:1035875894390161428>')
                       .replace('ステルスジャンプ', '<:gp15:1035875872055513088>')
                       .replace('受け身術', '<:gp16:1035875886798479370>')
                       .replace('サーマルインク', '<:gp17:1035875868431626291>')
                       .replace('追加ギアパワー倍化', '<:gp18:1035875896193732608>')
                       .replace('インク効率アップ(サブ)', '<:gp19:1035875863566221403>')
                       .replace('ヒト移動速度アップ', '<:gp20:1035875880507031562>')
                       .replace('スペシャル性能アップ', '<:gp21:1035875875448700928>')
                       .replace('イカダッシュ速度アップ', '<:gp22:1035875856553361438>')
                       .replace('スペシャル増加量アップ', '<:gp23:1035875873741619241>')
                       .replace('復活時間短縮', '<:gp24:1035875892775370752>')
                       .replace('アクション強化', '<:gp25:1035875854921764964>')
                       .replace('サブ影響軽減', '<:gp26:1035875865319456858>')
                       )
        try:
            jsonData["limitedGears"][5]["gear"]["additionalGearPowers"][1]["name"]
        except IndexError:
            embed4 = discord.Embed(
                        title = "通常ピックアップ",
                        color=0x457fce,
                        description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")
            embed4.add_field(name="ギアパワー", value=f"{henkan}|{hatena}", inline=True)
            embed4.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
            embed4.set_thumbnail(url=image)
            embed4.set_footer(text="API: https://splatoon3.ink/| イカコード3")
        else:
            embed4 = discord.Embed(
                        title = "通常ピックアップ",
                        color=0x457fce,
                        description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")  
            embed4.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}", inline=True)
            embed4.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
            embed4.set_thumbnail(url=image)
            embed4.set_footer(text="API: https://splatoon3.ink/| イカコード3")

            try:
                jsonData["limitedGears"][5]["gear"]["additionalGearPowers"][2]["name"]
            except IndexError:    
                embed4 = discord.Embed(
                            title = "通常ピックアップ",
                            color=0x457fce,
                            description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n") 
                embed4.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}", inline=True)
                embed4.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
                embed4.set_thumbnail(url=image)
                embed4.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            else:
                embed4 = discord.Embed(
                            title = "通常ピックアップ",
                            color=0x457fce,
                            description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")  
                embed4.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}{hatena}", inline=True)
                embed4.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
                embed4.set_thumbnail(url=image)
                embed4.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            

        url = "https://splatoon3.ink/data/gear.json"
        response = requests.get(url)
        jsonData = response.json()
        image = jsonData["data"]["gesotown"]["limitedGears"][4]["gear"]["image"]["url"]

        url2 = "https://api.koukun.jp/splatoon/3/geso/"
        ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
        headers = {"User-Agent": ua}
        response = requests.get(url2)
        jsonData = response.json()
        time = jsonData["limitedGears"][4]["saleEndTime"]
        t = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        n = t.strftime('%m/%d %H:%M')
        gear = jsonData["limitedGears"][4]["gear"]["name"]
        brand = jsonData["limitedGears"][4]["gear"]["brand"]["name"]
        power2 = jsonData["limitedGears"][4]["gear"]["primaryGearPower"]
        price = jsonData["limitedGears"][4]["price"]

        henkan = (power2
                       .replace('ラストスパート', '<:gp1:1035875883493380196>')
                       .replace('イカニンジャ', '<:gp2:1035875858197512223>')
                       .replace('インク効率アップ(メイン)', '<:gp3:1035875881991811084>')
                       .replace('スペシャル減少量ダウン', '<:gp4:1035875877059297290>')
                       .replace('スタートダッシュ', '<:gp5:1035875870189047878>')
                       .replace('カムバック', '<:gp6:1035875861670395904>')
                       .replace('復活ペナルティアップ', '<:gp7:1035875889793224707>')
                       .replace('サブ性能アップ', '<:gp8:1035875866569347207>')
                       .replace('対物攻撃力アップ', '<:gp9:1035875888526532698>')
                       .replace('逆境強化', '<:gp10:1035875898030833684>')
                       .replace('リベンジ', '<:gp11:1035875884919439460>')
                       .replace('スーパージャンプ時間短縮', '<:gp12:1035875878854475846>')
                       .replace('インク回復力アップ', '<:gp13:1035875859631972383>')
                       .replace('相手インク影響軽減', '<:gp14:1035875894390161428>')
                       .replace('ステルスジャンプ', '<:gp15:1035875872055513088>')
                       .replace('受け身術', '<:gp16:1035875886798479370>')
                       .replace('サーマルインク', '<:gp17:1035875868431626291>')
                       .replace('追加ギアパワー倍化', '<:gp18:1035875896193732608>')
                       .replace('インク効率アップ(サブ)', '<:gp19:1035875863566221403>')
                       .replace('ヒト移動速度アップ', '<:gp20:1035875880507031562>')
                       .replace('スペシャル性能アップ', '<:gp21:1035875875448700928>')
                       .replace('イカダッシュ速度アップ', '<:gp22:1035875856553361438>')
                       .replace('スペシャル増加量アップ', '<:gp23:1035875873741619241>')
                       .replace('復活時間短縮', '<:gp24:1035875892775370752>')
                       .replace('アクション強化', '<:gp25:1035875854921764964>')
                       .replace('サブ影響軽減', '<:gp26:1035875865319456858>')
                       )

        try:
            jsonData["limitedGears"][4]["gear"]["additionalGearPowers"][1]["name"]
        except IndexError:
            embed5 = discord.Embed(
                        title = "通常ピックアップ",
                        color=0x457fce,
                        description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")
            embed5.add_field(name="ギアパワー", value=f"{henkan}|{hatena}", inline=True)
            embed5.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
            embed5.set_thumbnail(url=image)
            embed5.set_footer(text="API: https://splatoon3.ink/| イカコード3")
        else:
            embed5 = discord.Embed(
                        title = "通常ピックアップ",
                        color=0x457fce,
                        description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")  
            embed5.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}", inline=True)
            embed5.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
            embed5.set_thumbnail(url=image)
            embed5.set_footer(text="API: https://splatoon3.ink/| イカコード3")

            try:
                jsonData["limitedGears"][4]["gear"]["additionalGearPowers"][2]["name"]
            except IndexError:    
                embed5 = discord.Embed(
                            title = "通常ピックアップ",
                            color=0x457fce,
                            description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n") 
                embed5.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}", inline=True)
                embed5.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
                embed5.set_thumbnail(url=image)
                embed5.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            else:
                embed5 = discord.Embed(
                            title = "通常ピックアップ",
                            color=0x457fce,
                            description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")  
                embed5.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}{hatena}", inline=True)
                embed5.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
                embed5.set_thumbnail(url=image)
                embed5.set_footer(text="API: https://splatoon3.ink/| イカコード3")

        url = "https://splatoon3.ink/data/gear.json"
        response = requests.get(url)
        jsonData = response.json()
        image = jsonData["data"]["gesotown"]["limitedGears"][3]["gear"]["image"]["url"]

        url2 = "https://api.koukun.jp/splatoon/3/geso/"
        ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
        headers = {"User-Agent": ua}
        response = requests.get(url2)
        jsonData = response.json()
        time = jsonData["limitedGears"][3]["saleEndTime"]
        t = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        n = t.strftime('%m/%d %H:%M')
        gear = jsonData["limitedGears"][3]["gear"]["name"]
        brand = jsonData["limitedGears"][3]["gear"]["brand"]["name"]
        power3 = jsonData["limitedGears"][3]["gear"]["primaryGearPower"]
        price = jsonData["limitedGears"][3]["price"]

        henkan = (power3
                       .replace('ラストスパート', '<:gp1:1035875883493380196>')
                       .replace('イカニンジャ', '<:gp2:1035875858197512223>')
                       .replace('インク効率アップ(メイン)', '<:gp3:1035875881991811084>')
                       .replace('スペシャル減少量ダウン', '<:gp4:1035875877059297290>')
                       .replace('スタートダッシュ', '<:gp5:1035875870189047878>')
                       .replace('カムバック', '<:gp6:1035875861670395904>')
                       .replace('復活ペナルティアップ', '<:gp7:1035875889793224707>')
                       .replace('サブ性能アップ', '<:gp8:1035875866569347207>')
                       .replace('対物攻撃力アップ', '<:gp9:1035875888526532698>')
                       .replace('逆境強化', '<:gp10:1035875898030833684>')
                       .replace('リベンジ', '<:gp11:1035875884919439460>')
                       .replace('スーパージャンプ時間短縮', '<:gp12:1035875878854475846>')
                       .replace('インク回復力アップ', '<:gp13:1035875859631972383>')
                       .replace('相手インク影響軽減', '<:gp14:1035875894390161428>')
                       .replace('ステルスジャンプ', '<:gp15:1035875872055513088>')
                       .replace('受け身術', '<:gp16:1035875886798479370>')
                       .replace('サーマルインク', '<:gp17:1035875868431626291>')
                       .replace('追加ギアパワー倍化', '<:gp18:1035875896193732608>')
                       .replace('インク効率アップ(サブ)', '<:gp19:1035875863566221403>')
                       .replace('ヒト移動速度アップ', '<:gp20:1035875880507031562>')
                       .replace('スペシャル性能アップ', '<:gp21:1035875875448700928>')
                       .replace('イカダッシュ速度アップ', '<:gp22:1035875856553361438>')
                       .replace('スペシャル増加量アップ', '<:gp23:1035875873741619241>')
                       .replace('復活時間短縮', '<:gp24:1035875892775370752>')
                       .replace('アクション強化', '<:gp25:1035875854921764964>')
                       .replace('サブ影響軽減', '<:gp26:1035875865319456858>')
                       )

        try:
            jsonData["limitedGears"][3]["gear"]["additionalGearPowers"][1]["name"]
        except IndexError:
            embed6 = discord.Embed(
                        title = "通常ピックアップ",
                        color=0x457fce,
                        description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")
            embed6.add_field(name="ギアパワー", value=f"{henkan}|{hatena}", inline=True)
            embed6.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
            embed6.set_thumbnail(url=image)
            embed6.set_footer(text="API: https://splatoon3.ink/| イカコード3")
        else:
            embed6 = discord.Embed(
                        title = "通常ピックアップ",
                        color=0x457fce,
                        description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")  
            embed6.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}", inline=True)
            embed6.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
            embed6.set_thumbnail(url=image)
            embed6.set_footer(text="API: https://splatoon3.ink/| イカコード3")

            try:
                jsonData["limitedGears"][3]["gear"]["additionalGearPowers"][2]["name"]
            except IndexError:    
                embed6 = discord.Embed(
                            title = "通常ピックアップ",
                            color=0x457fce,
                            description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n") 
                embed6.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}", inline=True)
                embed6.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
                embed6.set_thumbnail(url=image)
                embed6.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            else:
                embed6 = discord.Embed(
                            title = "通常ピックアップ",
                            color=0x457fce,
                            description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")  
                embed6.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}{hatena}", inline=True)
                embed6.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
                embed6.set_thumbnail(url=image)
                embed6.set_footer(text="API: https://splatoon3.ink/| イカコード3")

        url = "https://splatoon3.ink/data/gear.json"
        response = requests.get(url)
        jsonData = response.json()
        image = jsonData["data"]["gesotown"]["limitedGears"][2]["gear"]["image"]["url"]

        url2 = "https://api.koukun.jp/splatoon/3/geso/"
        ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
        headers = {"User-Agent": ua}
        response = requests.get(url2)
        jsonData = response.json()
        time = jsonData["limitedGears"][2]["saleEndTime"]
        t = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        n = t.strftime('%m/%d %H:%M')
        gear = jsonData["limitedGears"][2]["gear"]["name"]
        brand = jsonData["limitedGears"][2]["gear"]["brand"]["name"]
        power4 = jsonData["limitedGears"][2]["gear"]["primaryGearPower"]
        price = jsonData["limitedGears"][2]["price"]

        henkan = (power4
                       .replace('ラストスパート', '<:gp1:1035875883493380196>')
                       .replace('イカニンジャ', '<:gp2:1035875858197512223>')
                       .replace('インク効率アップ(メイン)', '<:gp3:1035875881991811084>')
                       .replace('スペシャル減少量ダウン', '<:gp4:1035875877059297290>')
                       .replace('スタートダッシュ', '<:gp5:1035875870189047878>')
                       .replace('カムバック', '<:gp6:1035875861670395904>')
                       .replace('復活ペナルティアップ', '<:gp7:1035875889793224707>')
                       .replace('サブ性能アップ', '<:gp8:1035875866569347207>')
                       .replace('対物攻撃力アップ', '<:gp9:1035875888526532698>')
                       .replace('逆境強化', '<:gp10:1035875898030833684>')
                       .replace('リベンジ', '<:gp11:1035875884919439460>')
                       .replace('スーパージャンプ時間短縮', '<:gp12:1035875878854475846>')
                       .replace('インク回復力アップ', '<:gp13:1035875859631972383>')
                       .replace('相手インク影響軽減', '<:gp14:1035875894390161428>')
                       .replace('ステルスジャンプ', '<:gp15:1035875872055513088>')
                       .replace('受け身術', '<:gp16:1035875886798479370>')
                       .replace('サーマルインク', '<:gp17:1035875868431626291>')
                       .replace('追加ギアパワー倍化', '<:gp18:1035875896193732608>')
                       .replace('インク効率アップ(サブ)', '<:gp19:1035875863566221403>')
                       .replace('ヒト移動速度アップ', '<:gp20:1035875880507031562>')
                       .replace('スペシャル性能アップ', '<:gp21:1035875875448700928>')
                       .replace('イカダッシュ速度アップ', '<:gp22:1035875856553361438>')
                       .replace('スペシャル増加量アップ', '<:gp23:1035875873741619241>')
                       .replace('復活時間短縮', '<:gp24:1035875892775370752>')
                       .replace('アクション強化', '<:gp25:1035875854921764964>')
                       .replace('サブ影響軽減', '<:gp26:1035875865319456858>')
                       )

        try:
            jsonData["limitedGears"][2]["gear"]["additionalGearPowers"][1]["name"]
        except IndexError:
            embed7 = discord.Embed(
                        title = "通常ピックアップ",
                        color=0x457fce,
                        description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")
            embed7.add_field(name="ギアパワー", value=f"{henkan}|{hatena}", inline=True)
            embed7.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
            embed7.set_thumbnail(url=image)
            embed7.set_footer(text="API: https://splatoon3.ink/| イカコード3")
        else:
            embed7 = discord.Embed(
                        title = "通常ピックアップ",
                        color=0x457fce,
                        description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")  
            embed7.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}", inline=True)
            embed7.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
            embed7.set_thumbnail(url=image)
            embed7.set_footer(text="API: https://splatoon3.ink/| イカコード3")

            try:
                jsonData["limitedGears"][2]["gear"]["additionalGearPowers"][2]["name"]
            except IndexError:    
                embed7 = discord.Embed(
                            title = "通常ピックアップ",
                            color=0x457fce,
                            description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n") 
                embed7.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}", inline=True)
                embed7.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
                embed7.set_thumbnail(url=image)
                embed7.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            else:
                embed7 = discord.Embed(
                            title = "通常ピックアップ",
                            color=0x457fce,
                            description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")  
                embed7.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}{hatena}", inline=True)
                embed7.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
                embed7.set_thumbnail(url=image)
                embed7.set_footer(text="API: https://splatoon3.ink/| イカコード3")

        url = "https://splatoon3.ink/data/gear.json"
        response = requests.get(url)
        jsonData = response.json()
        image = jsonData["data"]["gesotown"]["limitedGears"][1]["gear"]["image"]["url"]

        url2 = "https://api.koukun.jp/splatoon/3/geso/"
        ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
        headers = {"User-Agent": ua}
        response = requests.get(url2)
        jsonData = response.json()
        time = jsonData["limitedGears"][1]["saleEndTime"]
        t = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        n = t.strftime('%m/%d %H:%M')
        gear = jsonData["limitedGears"][1]["gear"]["name"]
        brand = jsonData["limitedGears"][1]["gear"]["brand"]["name"]
        power5 = jsonData["limitedGears"][1]["gear"]["primaryGearPower"]
        price = jsonData["limitedGears"][1]["price"]

        henkan = (power5
                       .replace('ラストスパート', '<:gp1:1035875883493380196>')
                       .replace('イカニンジャ', '<:gp2:1035875858197512223>')
                       .replace('インク効率アップ(メイン)', '<:gp3:1035875881991811084>')
                       .replace('スペシャル減少量ダウン', '<:gp4:1035875877059297290>')
                       .replace('スタートダッシュ', '<:gp5:1035875870189047878>')
                       .replace('カムバック', '<:gp6:1035875861670395904>')
                       .replace('復活ペナルティアップ', '<:gp7:1035875889793224707>')
                       .replace('サブ性能アップ', '<:gp8:1035875866569347207>')
                       .replace('対物攻撃力アップ', '<:gp9:1035875888526532698>')
                       .replace('逆境強化', '<:gp10:1035875898030833684>')
                       .replace('リベンジ', '<:gp11:1035875884919439460>')
                       .replace('スーパージャンプ時間短縮', '<:gp12:1035875878854475846>')
                       .replace('インク回復力アップ', '<:gp13:1035875859631972383>')
                       .replace('相手インク影響軽減', '<:gp14:1035875894390161428>')
                       .replace('ステルスジャンプ', '<:gp15:1035875872055513088>')
                       .replace('受け身術', '<:gp16:1035875886798479370>')
                       .replace('サーマルインク', '<:gp17:1035875868431626291>')
                       .replace('追加ギアパワー倍化', '<:gp18:1035875896193732608>')
                       .replace('インク効率アップ(サブ)', '<:gp19:1035875863566221403>')
                       .replace('ヒト移動速度アップ', '<:gp20:1035875880507031562>')
                       .replace('スペシャル性能アップ', '<:gp21:1035875875448700928>')
                       .replace('イカダッシュ速度アップ', '<:gp22:1035875856553361438>')
                       .replace('スペシャル増加量アップ', '<:gp23:1035875873741619241>')
                       .replace('復活時間短縮', '<:gp24:1035875892775370752>')
                       .replace('アクション強化', '<:gp25:1035875854921764964>')
                       .replace('サブ影響軽減', '<:gp26:1035875865319456858>')
                       )

        try:
            jsonData["limitedGears"][1]["gear"]["additionalGearPowers"][1]["name"]
        except IndexError:
            embed8 = discord.Embed(
                        title = "通常ピックアップ",
                        color=0x457fce,
                        description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")
            embed8.add_field(name="ギアパワー", value=f"{henkan}|{hatena}", inline=True)
            embed8.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
            embed8.set_thumbnail(url=image)
            embed8.set_footer(text="API: https://splatoon3.ink/| イカコード3")
        else:
            embed8 = discord.Embed(
                        title = "通常ピックアップ",
                        color=0x457fce,
                        description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")  
            embed8.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}", inline=True)
            embed8.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
            embed8.set_thumbnail(url=image)
            embed8.set_footer(text="API: https://splatoon3.ink/| イカコード3")

            try:
                jsonData["limitedGears"][1]["gear"]["additionalGearPowers"][2]["name"]
            except IndexError:    
                embed8 = discord.Embed(
                            title = "通常ピックアップ",
                            color=0x457fce,
                            description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n") 
                embed8.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}", inline=True)
                embed8.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
                embed8.set_thumbnail(url=image)
                embed8.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            else:
                embed8 = discord.Embed(
                            title = "通常ピックアップ",
                            color=0x457fce,
                            description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")  
                embed8.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}{hatena}", inline=True)
                embed8.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
                embed8.set_thumbnail(url=image)
                embed8.set_footer(text="API: https://splatoon3.ink/| イカコード3")

        url = "https://splatoon3.ink/data/gear.json"
        response = requests.get(url)
        jsonData = response.json()
        image = jsonData["data"]["gesotown"]["limitedGears"][0]["gear"]["image"]["url"]

        url2 = "https://api.koukun.jp/splatoon/3/geso/"
        ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
        headers = {"User-Agent": ua}
        response = requests.get(url2)
        jsonData = response.json()
        time = jsonData["limitedGears"][0]["saleEndTime"]
        t = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        n = t.strftime('%m/%d %H:%M')
        gear = jsonData["limitedGears"][0]["gear"]["name"]
        brand = jsonData["limitedGears"][0]["gear"]["brand"]["name"]
        power6 = jsonData["limitedGears"][0]["gear"]["primaryGearPower"]
        price = jsonData["limitedGears"][0]["price"]

        henkan = (power6
                       .replace('ラストスパート', '<:gp1:1035875883493380196>')
                       .replace('イカニンジャ', '<:gp2:1035875858197512223>')
                       .replace('インク効率アップ(メイン)', '<:gp3:1035875881991811084>')
                       .replace('スペシャル減少量ダウン', '<:gp4:1035875877059297290>')
                       .replace('スタートダッシュ', '<:gp5:1035875870189047878>')
                       .replace('カムバック', '<:gp6:1035875861670395904>')
                       .replace('復活ペナルティアップ', '<:gp7:1035875889793224707>')
                       .replace('サブ性能アップ', '<:gp8:1035875866569347207>')
                       .replace('対物攻撃力アップ', '<:gp9:1035875888526532698>')
                       .replace('逆境強化', '<:gp10:1035875898030833684>')
                       .replace('リベンジ', '<:gp11:1035875884919439460>')
                       .replace('スーパージャンプ時間短縮', '<:gp12:1035875878854475846>')
                       .replace('インク回復力アップ', '<:gp13:1035875859631972383>')
                       .replace('相手インク影響軽減', '<:gp14:1035875894390161428>')
                       .replace('ステルスジャンプ', '<:gp15:1035875872055513088>')
                       .replace('受け身術', '<:gp16:1035875886798479370>')
                       .replace('サーマルインク', '<:gp17:1035875868431626291>')
                       .replace('追加ギアパワー倍化', '<:gp18:1035875896193732608>')
                       .replace('インク効率アップ(サブ)', '<:gp19:1035875863566221403>')
                       .replace('ヒト移動速度アップ', '<:gp20:1035875880507031562>')
                       .replace('スペシャル性能アップ', '<:gp21:1035875875448700928>')
                       .replace('イカダッシュ速度アップ', '<:gp22:1035875856553361438>')
                       .replace('スペシャル増加量アップ', '<:gp23:1035875873741619241>')
                       .replace('復活時間短縮', '<:gp24:1035875892775370752>')
                       .replace('アクション強化', '<:gp25:1035875854921764964>')
                       .replace('サブ影響軽減', '<:gp26:1035875865319456858>')
                       )

        try:
            jsonData["limitedGears"][0]["gear"]["additionalGearPowers"][1]["name"]
        except IndexError:
            embed9 = discord.Embed(
                        title = "通常ピックアップ",
                        color=0x457fce,
                        description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")
            embed9.add_field(name="ギアパワー", value=f"{henkan}|{hatena}", inline=True)
            embed9.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
            embed9.set_thumbnail(url=image)
            embed9.set_footer(text="API: https://splatoon3.ink/| イカコード3")
        else:
            embed9 = discord.Embed(
                        title = "通常ピックアップ",
                        color=0x457fce,
                        description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")  
            embed9.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}", inline=True)
            embed9.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
            embed9.set_thumbnail(url=image)
            embed9.set_footer(text="API: https://splatoon3.ink/| イカコード3")

            try:
                jsonData["limitedGears"][0]["gear"]["additionalGearPowers"][2]["name"]
            except IndexError:    
                embed9 = discord.Embed(
                            title = "通常ピックアップ",
                            color=0x457fce,
                            description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n") 
                embed9.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}", inline=True)
                embed9.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
                embed9.set_thumbnail(url=image)
                embed9.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            else:
                embed9 = discord.Embed(
                            title = "通常ピックアップ",
                            color=0x457fce,
                            description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")  
                embed9.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}{hatena}", inline=True)
                embed9.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
                embed9.set_thumbnail(url=image)
                embed9.set_footer(text="API: https://splatoon3.ink/| イカコード3")

        page = [embed1,embed2,embed3,embed4,embed5,embed6,embed7,embed8,embed9]
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
    bot.add_cog(cmd(bot))