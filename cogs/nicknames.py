import nextcord
from nextcord.ext import commands
from nextcord import Interaction

guildID = 806373333560983562


##changes nickname of author in server
class ChangeNickname(commands.Cog):
    def __init__(self,dis_bot):
        self.dis_bot = dis_bot

    
    @nextcord.slash_command(name = 'nickname', description = "Enter new nickname or 'remove' to remove current nickname",guild_ids=[guildID])
    async def change_nickname(self, interaction:Interaction, nick_name:str):

        if nick_name == 'remove':
            await interaction.user.edit(nick = None)
        else:
            await interaction.user.edit(nick = nick_name)
        
        await interaction.response.send_message("Nickname succesfully changed!")


def setup(bot):
    bot.add_cog(ChangeNickname(bot))