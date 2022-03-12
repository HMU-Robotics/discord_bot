

import nextcord
from nextcord import Interaction
from nextcord.ext import commands

guildID = 806373333560983562


class Test(commands.Cog):
    def __init__(self,client):
        self.client = client
        

    @nextcord.slash_command(name='hello',description="Test",guild_ids=[guildID])
    async def test(self,interaction:Interaction):
        print(interaction.message)
        await interaction.response.send_message("Test")
    


def setup(bot):
    bot.add_cog(Test(bot))