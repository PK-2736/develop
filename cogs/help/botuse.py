import discord
import asyncio
from discord.ext import commands

print("botuseの読み込み完了")

class botuse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return 
        if message.content == "IkacordBOTの使い方":
            global embedbotuse
            embedbotuse = discord.Embed( 
                            title="IkacordBOTの使い方",
                            description="バンカラ(オープン)のステージ情報を表示します"
                                            "```/すてオープン```\n"
                                            "バンカラ(チャレンジ)のステージ情報を表示します"
                                            "```/すてオープン```\n"
                                            "レギュラーのステージ情報を表示します"
                                            "```/すてレギュラー```\n"
                                            "サーモンランのステージ情報を表示します"
                                            "```/すてバイト```\n"
                                            "ランダムに武器を表示します"
                                            "```/ブキ```\n"
                                            "ブランド別ギア表を表示します"
                                            "```/ギア表```\n"
                                            "フレンドコードを保存します"
                                            "```/ふれこ登録 (自分のフレンドコード)```\n"
                                            "フレンドコードを検索します"
                                            "```/ふれこ検索 (対象の人をメンション)```\n"
                                            "自分のフレンドコードを削除します"
                                            "```/ふれこ削除 (自分をメンション) (自分のフレンドコード)```\n"
                                            "バンカラ募集します"
                                            "```/ぼしゅうバンカラ```\n"
                                            "レギュラー募集します"
                                            "```/ぼしゅうレギュラー```\n"
                                            "バイト募集します"
                                            "```/ぼしゅうバイト```\n"
                                            "なんでも募集します"
                                            "```/ぼしゅうなんでも```\n"
                                            "フェス募集します(フェス期間のみ)"
                                            "```/ぼしゅうフェス(各陣営)```\n"
                                            # "読み上げを開始"
                                            # "```/join```\n"
                                            # "読み上げを終了"
                                            # "```/disconnect```\n"
                                            # "単語登録"
                                            # "```/dictionary add before: after:```\n"
                                            # "話者変更"
                                            # "```/setvoice 話者:```\n"
                                            # "読み上げbotのコマンドヘルプ"
                                            # "```/dictionary help```\n"                                                                                                                                   
                                            "ikacordのコマンド別helpを表示します"
                                            "```/help```"
                                            "bot情報を表示します"
                                            "```/ikacord```\n"                                                                                       
                            ,color=0x30f05d, )

            channel = self.bot.get_channel(982600408704892998)

            await channel.send(embed=embedbotuse)

def setup(bot):
    bot.add_cog(botuse(bot))

