import nextcord
from nextcord import Interaction
from nextcord.ext import commands



import os
from dotenv import load_dotenv,find_dotenv


load_dotenv(find_dotenv())
guildID = os.getenv("guild_test")

## change/create roles for users
class ChangeRoles(commands.Cog):
    def __init__(self,dis_user):
        self.dis_user = dis_user


    @nextcord.slash_command(guild_ids = [guildID])
    async def role_edit(self, interaction: Interaction):

        ## stays empty for subcommands
        ...


    ## changes user's(one or many) role
    @role_edit.subcommand(name = 'Add new roles',description = "Adds users to a new role(can me more than 1)")
    async def role_add(self, interaction:Interaction, users_id:str, roles_id:str):
        guild = interaction.guild
        users_id_list = users_id.split()
        users_id_list = list(map(int,users_id_list))
        roles_id_list = roles_id.split()
        roles_id_list = list(map(int,roles_id_list))
        roles_toapply = []
        
        ## gets roles from server
        for server_role_id in guild.roles:
            for role_id in roles_id_list:
                if role_id == server_role_id.id:
                    roles_toapply.append(server_role_id)


        ## edits user's roles
        ## REPLACES OLD ROLES THEY HAVE TO BE READDED
        for user_id in users_id_list:
            member = await guild.fetch_member(user_id)
            await member.edit(roles = roles_toapply)

        await interaction.response.send_message("Roles succesfully added")


    ## creates new role with permissions
    @role_edit.subcommand(name = 'Create new role',description = "Create new role with permissions")
    ## currently only has "general" permissions
    async def role_create(self, interaction: Interaction, role_name: str, shown: bool):
        guild = interaction.guild
        role_permissions = interaction.permissions.general()

        await guild.create_role(name = role_name, permissions = role_permissions, hoist=shown)
        await interaction.response.send_message("Role created succesfully")
        


    ## edits role's permissions
    @role_edit.subcommand(name = 'Edit role permissions',description = "Edit role's permissions")
    async def role_perm(self, interaction: Interaction, role_id: str, perm: str, shown: bool):
        guild = interaction.guild
        role_id = int(role_id)
        ## currently only permissions allowed are general
        if perm == "general":
            permission = interaction.permissions.general()
        
        for role in guild.roles:
            if role.id == role_id:
                await role.edit(permissions = permission, hoist = shown)
        await interaction.response.send_message("Role was edited succesfully")
        


def setup(bot):
    bot.add_cog(ChangeRoles(bot))