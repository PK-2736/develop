import discord
from discord.ext import commands
from discord.ui import Button, View
from datetime import datetime
import io
import re
from PIL import Image, ImageFont, ImageDraw
import textwrap
import requests
from festint import *

from cogs import guild_ids

print("rectmantaroの読み込み完了")

class Spla3View(discord.ui.View):
    def __init__(self, initiator_id):
        super().__init__(timeout=None)
        self.initiator_id = initiator_id

    @discord.ui.button(style=discord.ButtonStyle.green, label="参加", custom_id="join")
    async def callback_join(self, button: Button, interaction: discord.Interaction):
        for child in self.children:
            child.disabled = True

        embed = interaction.message.embeds[0]
        if embed and len(embed.fields) == 0:
            embed.add_field(name="参加者リスト", value=f"{interaction.user.mention} {datetime.now().strftime('%H:%M')}", inline=True)

        for idlist in embed.fields[0].value.split("\n"):
            match = re.search(f"{interaction.user.id}", idlist)

        if match:
            embed2 = discord.Embed(description=f"{interaction.user.name}は既に参加しています")
            await interaction.response.send_message(embed=embed2, ephemeral=True)
        else:
            users = [interaction.user.mention]
            cm = embed.fields[0].value
            tmp = "\n".join([str(user) for user in users])
            summon = tmp if tmp else "なし"
            s = embed.fields[0].name
            result = re.sub(r"\D", "", s)
            cut = int(result) + 1
            time = datetime.now().strftime("%H:%M")
            embed.set_field_at(0, name=f"参加者リスト `[{cut}]`", value=f"{cm}\n{summon} {time}", inline=False)
            await interaction.response.edit_message(embed=embed)
            embed = discord.Embed()
            embed.set_author(name=f"{interaction.user.name}が参加しました", icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
            await interaction.message.reply(f"{interaction.message.interaction.user.mention}{interaction.user.mention}", embed=embed, delete_after=120.0)       #募集に参加ボタン

    @discord.ui.button(style=discord.ButtonStyle.blurple, label="取り消し", custom_id="remove")
    async def callback_remove(self, button: Button, interaction: discord.Interaction):
        for child in self.children:
            child.disabled = True

        embed = interaction.message.embeds[0]
        for idlist in embed.fields[0].value.split("\n"):
            match = re.search(f"{interaction.user.id}", idlist)

        if match:
            s = embed.fields[0].name
            result = re.sub(r"\D", "", s)

            if int(result) == 1:
                embed = discord.Embed(description="参加者がいなくなるため取り消しできません。しめを押してください。")
                await interaction.response.send_message(embed=embed, ephemeral=True)
            else:
                cm = embed.fields[0].value
                pattern = r'\s(\d{2}):(\d{2})'
                a = re.sub(f"<@{interaction.user.id}>{pattern}", " ", cm)
                cut = int(result) - 1
                embed.set_field_at(0, name=f"参加者リスト `[{cut}]`", value=f"{a}", inline=False)
                await interaction.response.edit_message(embed=embed)
                embed = discord.Embed()
                embed.set_author(name=f"{interaction.user.name}が参加を取り消しました", icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
                await interaction.message.reply(f"{interaction.message.interaction.user.mention}{interaction.user.mention}", embed=embed, delete_after=120.0)   #募集取り消しボタン

        else:
            embed = discord.Embed(description="参加していないため取り消せません。募集主は取り消しできません。")
            await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(style=discord.ButtonStyle.red, label="しめ", custom_id="sime")
    async def callback_sime(self, button: Button, interaction: discord.Interaction):
        if interaction.user.id != self.initiator_id:
            embed = discord.Embed(description="募集主ではないので〆ができません。")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return  # コマンドを実行したユーザー以外は処理しない

        interaction.permissions.use_application_commands = True
        for child in self.children:
            child.disabled = True

        embed = discord.Embed()
        embed.set_author(name=f"{interaction.user.name}の募集〆", icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
        await interaction.message.reply(embed=embed)
        await interaction.response.edit_message(view=self)   #募集締めボタン


    @discord.ui.button(style=discord.ButtonStyle.grey, label="ステージ", custom_id="stage")
    async def callback_stage(self, button: Button, interaction: discord.Interaction):
        await interaction.response.defer()
        url = "https://spla3.yuu26.com/api/fest/schedule"
        ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
        headers = {"User-Agent": ua}
        response = requests.get(url, headers=headers)
        jsonData = response.json()
        stages = jsonData["results"][0]["stages"]
        time = jsonData["results"][0]["start_time"]
        time2 = jsonData["results"][0]["end_time"]
        t = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
        n = t.strftime('%H:%M')
        t2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S%z')
        n2 = t2.strftime('%H:%M')

        images = []
        for stage in stages:
            image = stage["image"]
            images.append(Image.open(io.BytesIO(requests.get(image).content)))

        img = Image.new('RGB', (800, 200), (0, 0, 0))
        img.paste(images[0], (405, 0))
        img.paste(images[1], (0, 0))

        img_binary = io.BytesIO()
        img.save(img_binary, format='PNG')
        img_binary.seek(0)

        embed = discord.Embed(
            title="フェスマッチ",
            color=0xeae1dc,
            description=f"**{n}から{n2}まで**\n\n**{stages[0]['name']}**\n**{stages[1]['name']}**"
        )
        file = discord.File(img_binary, filename='image.png')
        embed.set_image(url="attachment://image.png")
        embed.set_thumbnail(url="https://img.gamewith.jp/img/17cd16891d1d50e569e19879057dfa26.png")
        embed.set_footer(text="API: https://spla3.yuu26.com | イカコード3")  #ステージ情報確認ボタン

        await interaction.followup.send(embed=embed, file=file, ephemeral=True)

class RectmantaroModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="時間", required=False))
        self.add_item(discord.ui.InputText(label="募集人数"))
        self.add_item(discord.ui.InputText(label="通話の有無"))
        self.add_item(discord.ui.InputText(label="募集内容", style=discord.InputTextStyle.long, required=False))

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()

        img = Image.open("images/fest/mantaro.png")
        draw = ImageDraw.Draw(img)
        font_path = "data/Splatfont.ttf"
        font = ImageFont.truetype(font_path, 70)
        time = self.children[0].value or "集まり次第"
        draw.text((1050, 382), f"{self.children[0].value}{time}", (0, 0, 0), font=font)
        draw.text((1050, 685), self.children[1].value, (0, 0, 0), font=font)
        draw.text((1050, 995), self.children[2].value, (0, 0, 0), font=font)

        content = self.children[3].value or "記載なし"
        wrap_list = textwrap.wrap(f"{self.children[3].value}{content}", 11)
        font_path2 = "data/05TogeGothic-SemiBold.otf"
        font2 = ImageFont.truetype(font_path2, 52)
        line_counter = 0
        for line in wrap_list:
            y = line_counter * 60 + 460
            draw.multiline_text((260, y), line, fill=(255, 255, 255), font=font2)
            line_counter += 1
        img_binary = io.BytesIO()
        img.save(img_binary, format='PNG')
        img_binary.seek(0)
        f = discord.File(img_binary, filename='image.png')

        color = discord.Colour(int(Charlie_color.strip("#"), 16))  
        embed = discord.Embed(
            timestamp=datetime.now(),
            color=color
        )
        embed.add_field(name="参加者リスト `[1]`", value=f"{interaction.user.mention} {datetime.now().strftime('%H:%M')}", inline=False)
        embed.set_thumbnail(url=f"{Charlie_image}")
        embed.set_footer(text='イカコード3 | スプラ募集')
        await interaction.followup.send(f"{interaction.user.mention}が<@&{Charlie_role}>募集中！", embed=embed, file=f,view=Spla3View(interaction.user.id))

class Mantarocmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name=f"ぼしゅう{Charlie_name}陣営", guild_ids=guild_ids, description=f"{Charlie_name}陣営のフェス募集を取り付けます。")
    async def mantarorect(self, interaction: discord.Interaction):
        if interaction.channel.id not in [Charlie_channel, 802345513495822339, 803028814736392192]:
            return await interaction.respond(f"エラー：{Charlie_name}陣営募集コマンドは <#{Charlie_channel}> で実行してください。", ephemeral=True)
        
        modal = RectmantaroModal(title="募集の詳細を説明")
        await interaction.response.send_modal(modal)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot and message.channel.id in [Charlie_channel, 802345513495822339, 803028814736392192]:
            rectword = [f'が<@&{Charlie_role}>募集中！']
            for word in rectword:
                if word in message.content:
                    await message.channel.send(f"@everyone<@&{Charlie_role}>", delete_after=5)

def setup(bot: commands.Bot):
    bot.add_cog(Mantarocmd(bot=bot))