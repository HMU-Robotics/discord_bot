from random import random ,randint
from nextcord.ext import commands
import nextcord
import os
from dotenv import load_dotenv , find_dotenv
import asyncpraw




load_dotenv(find_dotenv())
guildID = os.getenv("guild_test")

load_dotenv(find_dotenv())
REDDIT_APP_ID = os.getenv("REDDIT_APP_ID")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")

class Fun(commands.Cog):
    def __init__(self,client):
        self.client = client
        self.reddit = None
        if REDDIT_APP_ID and REDDIT_SECRET:
            self.reddit = asyncpraw.Reddit(client_id = REDDIT_APP_ID , client_secret=REDDIT_SECRET,
            user_agent="HMU_Robotics_bot:%s:1.0"% REDDIT_APP_ID)


    @nextcord.slash_command(name='engineermemes',description="post a random meme",guild_ids=[guildID])
    async def memes(self,ctx:commands.Context):
        async with ctx.channel.typing():
            # chosen_subreddit = "engineeringmemes"
            # submissions = self.reddit.subreddit(chosen_subreddit).hot()
            # post_to = randint(1,10)
            subreddit = await self.reddit.subreddit("engineeringmemes")
            choice = randint(1,9)
            count = 0
            async for submission in subreddit.hot(limit=10):
                if count == choice:
                    await ctx.send(submission.url)
                    break
                else:
                    count += 1
            # for i in range(0,post_to):
            #     submissions = next(x for x in submissions if not x.stickied)
            # await ctx.send(submissions.url)




def setup(bot):
    bot.add_cog(Fun(bot))