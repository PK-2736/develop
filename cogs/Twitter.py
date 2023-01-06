import tweepy
from discord.ext import commands,tasks
import re
import discord
from datetime import datetime
from enum import Flag

print("twitterの読み込み完了")

class twitter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.loop.start()

    @tasks.loop(seconds=60)
    async def loop(self):

            AK = 'oFp2vNF9F6NPWytADGLwgQy9x'
            AS = 'MTKPhwT3AgoAID77rK0PInhJojeUSlySasTgD9W06HTC2iWdIB'
            AT = '1289065528904921088-tuxMchBmY7Fs7Hf2mKRqn6iWnlps6K'
            ATS = 'VCQqWPcbPUr1gWfoh6RpFJAwhLoXfEEXB0XpWFzYq5lzS'

            auth = tweepy.OAuthHandler(AK, AS)
            auth.set_access_token(AT, ATS)
            api = tweepy.API(auth, wait_on_rate_limit = True)
            account = "@SplatoonJP"

            flag = True
            with open('data/tweet.txt', 'r') as f:
                tweetid = f.read()
                tweet = api.user_timeline(screen_name=account,tweet_mode='extended',count=1)[0]
                match = re.fullmatch(f"{tweet.id}",tweetid)

                if match:
                    flag = False
                    return
                            
                if flag:
                    with open('data/tweet.txt', 'w') as f:
                        f.write(f'{tweet.id}')
                    embed = discord.Embed(
                                                title = "イカ研究所",
                                                description=f"{tweet.created_at}\n{tweet.full_text}",
                                                timestamp=datetime.now())
                    #embed.set_author(name=tweet.user.name, icon_url=tweet.user.profile_image_url(format="png", static_format="png"))
                    embed.set_footer(text='twitter')
                    channel = self.bot.get_channel(982946286493913098)
                    await channel.send(embed=embed)                
      
def setup(bot):
    bot.add_cog(twitter(bot))
                