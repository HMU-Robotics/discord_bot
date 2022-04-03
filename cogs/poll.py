import nextcord
from nextcord import Interaction
from nextcord.ext import commands

guildID = 806373333560983562

class Poll(commands.Cog):
    def __init__(self,client):
        self.client = client

        self.emojiLetters = [
            "\N{REGIONAL INDICATOR SYMBOL LETTER A}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER B}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER C}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER D}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER E}", 
            "\N{REGIONAL INDICATOR SYMBOL LETTER F}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER G}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER H}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER I}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER J}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER K}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER L}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER M}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER N}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER O}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER P}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER Q}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER R}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER S}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER T}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER U}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER V}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER W}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER X}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER Y}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER Z}"
        ]



    def getOptions(self,options):
        optionsText = options.split('//')
        print(optionsText)
        return optionsText


    @nextcord.slash_command(name='poll',description="creates a poll",guild_ids=[guildID])
    async def poll(self,ctx:commands.Context , title , description ,text):
        optionsText = self.getOptions(text)
        count = 0
        colour = 0x1d21ea
        finalmsg = ""
        for numText in optionsText:
            finalmsg += f"{self.emojiLetters[count]} )  {numText}\n\n"
            count += 1
        e = nextcord.Embed(title="**"+title+"**",description=description + "\n\n" + finalmsg,colour= colour)
        embed = await ctx.channel.send(embed=e)
        for x in range(0,count,1):
            await embed.add_reaction(self.emojiLetters[x])

def setup(bot):
    bot.add_cog(Poll(bot))