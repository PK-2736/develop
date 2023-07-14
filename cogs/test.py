import asyncio
import aiohttp
import ipaddress
import json
import logging
import os
import platform
import subprocess
import sys
import enum
import traceback

import discord
from discord.ext import commands
from discord import SlashCommandGroup, ApplicationContext, Option, StageChannel, TextChannel, VoiceChannel
from discord.commands import slash_command, Option
from cogs import guild_ids
import requests
import datetime


class Splatoon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @slash_command(name='aaa', guild_ids = guild_ids, description='aaa')
    async def geartest(self, interaction):
        _res = requests.get('https://splatoon3.ink/data/locale/ja-JP.json')
        data = json.loads(_res.content)
        dict_stages = data['stages']
        dict_rules  = data['rules']
        dict_weapons = data['weapons']
        response = requests.get('https://splatoon3.ink/data/schedules.json')
        data = json.loads(response.content)
        dict_result = {}
        dict_rules = {}
        nawabari = data['data']['regularSchedules']['nodes']
        for item in nawabari:
                        time            = item["startTime"]
                        timestamp       = datetime.datetime.fromisoformat(time.rstrip('Z'))
                        delta           = datetime.timedelta(hours=9)
                        timestamp_local = timestamp + delta
                        stage_id1       = item["regularMatchSetting"]["vsStages"][0]["id"]
                        stage_id2       = item["regularMatchSetting"]["vsStages"][1]["id"]
                        rule_id         = item["regularMatchSetting"]["vsRule"]["id"]
                        dict_result[timestamp_local] = [f'ナワバリバトル：{dict_stages[stage_id1]["name"]} / {dict_stages[stage_id2]["name"]}']
                        dict_rules[timestamp_local] = [f'ルール：{dict_rules[rule_id]["id"]["name"]}']

                        embed = discord.Embed(
                                            title = "レギュラーマッチ",
                                            color=0x00ff00,
                                            description=f"{dict_result[timestamp_local]}\nルール：{dict_rules[timestamp_local]}")
                        file = discord.File(img_binary, filename='image.png')
                        embed.set_image(url="attachment://image.png")
                        embed.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/4/4c/Mode_Icon_Regular_Battle_2.png")
                        embed.set_footer(text="API: https://spla3.yuu26.com| イカコード3")

    
        await interaction.response.defer(ephemeral=True)
        await interaction.send(embed=embed)


def setup(bot, **kwargs):
    bot.add_cog(Splatoon(bot, **kwargs))