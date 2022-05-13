import nextcord
from nextcord.ext import commands
from nextcord import Interaction

import os
from dotenv import load_dotenv,find_dotenv


load_dotenv(find_dotenv())
guildID = os.getenv("guild_test")



class ChangeNickname(commands.Cog):
    def __init__(self,dis_bot):
        self.dis_bot = dis_bot



    ## mass change nicknames for server members (admin only)
    @nextcord.slash_command(name="change_members_nicknames", description="Mass changes guild's member nicknames", guild_ids=[guildID], default_permission=False)
    async def change_members_nicknames(self, interaction: Interaction,users_ids:str, nickname_list:str):
        nickname_list = nickname_list.split()
        guild = interaction.guild
        users_ids = users_ids.split()
        users_ids = list(map(int,users_ids))

        ## compiles userIds with their nickname in dictionary
        user_dict = dict(zip(users_ids, nickname_list))

        for user, nickname in user_dict.items():
            await guild.get_member(user).edit(nick=nickname)
        
        await interaction.response.send_message("Server nicknames changed succesfully")




def setup(bot):
    bot.add_cog(ChangeNickname(bot))