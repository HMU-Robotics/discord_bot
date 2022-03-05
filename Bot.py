import os
from discord.ext import commands
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())
token = os.getenv("TOKEN")



bot = commands.Bot(command_prefix="!")

for filename in os.listdir("./commands"):
    if filename.endswith(".py") and filename !="__init__.py":
        bot.load_extension(f'commands.{filename[:-3]}')

print("I am online!")
bot.run(token)