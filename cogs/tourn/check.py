from email import message
import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import io
import re
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from discord.ui import Button, View, Select
from datetime import datetime
import textwrap
import requests
from discord.utils import get
import json
import codecs

from cogs import guild_ids

print("checkの読み込み完了")

class rectcheck(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="名前", style=discord.InputTextStyle.short, required=False))
        self.add_item(discord.ui.InputText(label="ウデマエ", style=discord.InputTextStyle.short, required=False))
        self.add_item(discord.ui.InputText(label="一言", style=discord.InputTextStyle.long, required=False))

    async def callback(self,interaction: discord.Interaction):
        searchfile = open("data/user.txt")
        for line in searchfile:
                search = re.search(r'\d{18}', line)
                user_id = search.group(0)
                guild = interaction.guild
                if f'{user_id}' in line:

                    sample_dict = {'名前': f'{self.children[0].value}', 'ウデマエ': f'{self.children[1].value}', '一言': f'{self.children[2].value}'}

                    with codecs.open(f'data/{user_id}.json', 'r', encoding="utf-8") as f:
                        read_data = json.load(f)
                        save_data = [read_data, sample_dict]
                    with codecs.open(f'data/{user_id}.json', 'w', encoding="utf-8") as f:
                        json.dump(save_data, f, indent=2, ensure_ascii=False)

                    input_date = int(user_id)
                    user = guild.get_member(input_date)
                    await user.send("大会参加応募が来ました。",file=discord.File(f'data/{user_id}.json'))
                    await interaction.response.send_message(f"大会に申し込みました。", ephemeral=True)
                
                else:
                    await interaction.response.send_message(f"えら", ephemeral=True)
                
class rectmou(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self.add_item(discord.ui.InputText(label="募集内容", style=discord.InputTextStyle.long, required=False))

    async def callback(self,interaction: discord.Interaction):
        searchfile = open("data/user.txt")
        for line in searchfile:
                search = re.search(r'\d{18}', line)
                user_id = search.group(0)
                guild = interaction.guild
                if f'{user_id}' in line:
                    input_date = int(user_id)
                    user = guild.get_member(input_date)
                    await user.send(f"{self.children[0].value}")
                    await interaction.response.send_message(f"{self.children[0].value}", ephemeral=True)
                    return
                else:
                    await interaction.response.send_message(f"えら", ephemeral=True)
                    return

class spla3(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        style=discord.ButtonStyle.green,
        label="参加申し込み",
        custom_id="mou"
    )
    async def callback_mou(self, button: Button, interaction: discord.Interaction):
            modal = rectcheck(title="申込み内容")
            #modal.add_item(discord.ui.Select(min_values=1, max_values=1, options=[discord.SelectOption(label='A'), discord.SelectOption(label='B')]))
            await interaction.response.send_modal(modal)

    @discord.ui.button(
        style=discord.ButtonStyle.grey,
        label="お問い合わせ",
        custom_id="toi"
    )
    async def callback_toi(self, button: Button, interaction: discord.Interaction):
            modal = rectmou(title="問い合わせ内容")
            #modal.add_item(discord.ui.Select(min_values=1, max_values=1, options=[discord.SelectOption(label='A'), discord.SelectOption(label='B')])
            await interaction.response.send_modal(modal)

class check(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="ぼしゅう大会" ,guild_ids=guild_ids, description="大会の募集フォームを作成します。")
    async def modal(self,interaction:discord.Interaction):

        path = 'data/user.txt'
        f = open(path, 'w')
        f.write(f'{interaction.user.id}')
        f.close()
        with codecs.open(f'data/{interaction.user.id}.json', 'w', 'utf-8') as f:
            sample_dict = {'主催者': f'{interaction.user.name}'}
            json.dump(sample_dict, f, ensure_ascii=False)
        await interaction.response.send_message(f"申込みフォームです。",view=spla3())

def setup(bot: commands.Bot):
    bot.add_cog(check(bot=bot))