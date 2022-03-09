import os
from sys import intern
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from dotenv import load_dotenv,find_dotenv


load_dotenv(find_dotenv())
token = os.getenv("TOKEN")


interns = nextcord.Intents.default()
interns.members = True
bot = commands.Bot(command_prefix="!",interns=interns)

@bot.event
async def on_ready():
    print(f'{bot.user} has logged in.')
    
#loads cogs
initial_extensions = []

for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename !="__init__.py":
            initial_extensions.append(f'cogs.{filename[:-3]}')

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)
############################################################################

print("I am online!")
bot.run(token)