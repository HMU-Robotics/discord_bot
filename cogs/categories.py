import nextcord
from nextcord.ext import commands
from nextcord import Interaction


guildID = 806373333560983562


class Categories(commands.Cog):
    def __init__(self,idk):
        self.idk = idk


    ## main command for later subcommands
    @nextcord.slash_command(guild_ids=[guildID])
    async def category_manage(self, interaction: Interaction):
        ## has to remain empty for subcommands
        pass


    ## creates category
    @category_manage.subcommand(name="create_category",description="Creates a new category with text and voice channels")
    async def category_create(self, interaction: Interaction,category_name:str, textchannel:bool, vchannel:bool):
        guild = interaction.guild

        dis_category = await guild.create_category(name=category_name)
        ## adds default text channel
        if textchannel is True:
            await guild.create_text_channel(name="general", category=dis_category)
        if vchannel is True:
            await guild.create_voice_channel(name="voice", category=dis_category)
        await interaction.response.send_message("Category created succesfully")


    ## creates role specific category
    @category_manage.subcommand(name="create_role_category",description="Creates category for certain roles")
    async def category_secret_create(self, interaction: Interaction,category_name:str,roles_id:str,textchannel:bool,vchannel:bool):
        guild = interaction.guild
        role_id_list = roles_id.split()
        role_id_list = list(map(int,role_id_list))
        role_list = []

        for role_id in role_id_list:
            role_list.append(guild.get_role(role_id))


        overwrite_rules = {
            guild.default_role: nextcord.PermissionOverwrite(read_messages=False),
        }

        ## adds or updates new roles who can view the category channel
        for role_name in role_list:
            new_dict ={role_name: nextcord.PermissionOverwrite(read_messages=True)}
            overwrite_rules.update(new_dict)
        

        secret_category = await guild.create_category(name=category_name,overwrites=overwrite_rules)
        ##adds default channels
        if textchannel is True:
            await guild.create_text_channel(name="general",category=secret_category)
        if vchannel is True:
            await guild.create_voice_channel(name="voice",category=secret_category)
        
        await interaction.response.send_message("Category created succesfully")


    ## deletes category
    @category_manage.subcommand(name="delete_category",description="Deletes category")
    async def category_delete(self, interaction:Interaction,category_id:str):
        guild = interaction.guild
        category_id = int(category_id)

        category = guild.get_channel(category_id)
        await category.delete()
        await interaction.response.send_message("Category deleted succesfully")
    

    ## edits category name
    @category_manage.subcommand(name="edit_category",description="Edits category")
    async def category_edit(self, interaction:Interaction,category_id:str,new_name:str):
        guild = interaction.guild
        category_id = int(category_id)
        await guild.get_channel(category_id).edit(name=new_name)
        await interaction.response.send_message("Category edited succesfully")


    @nextcord.slash_command(guild_ids=[guildID])
    async def textchannel_manage(self, interaction:Interaction):
        ## leave empty for subcommands
        pass


    ## text channel create
    @textchannel_manage.subcommand(name="textchannel_create",description="Create new textchannel for category")
    async def textchannel_create(self, interaction:Interaction,text_name:str, category_id:str):
        guild = interaction.guild
        category_id = int(category_id)
        category_sel = guild.get_channel(category_id)

        await guild.create_text_channel(name=text_name,category=category_sel)
        await interaction.response.send_message("Text channel created succesfully")

    
    ## text channel delete
    @textchannel_manage.subcommand(name="textchannel_delete",description="Deletes textchannel")
    async def textchannel_delete(self, interaction:Interaction,tchannel_id:str):
        guild = interaction.guild
        tchannel_id = int(tchannel_id)
        tchannel_sel = guild.get_channel(tchannel_id)
        
        await tchannel_sel.delete()
        await interaction.response.send_message("Textchannel deleted succesfully")

    ## voice channel subcommands
    @nextcord.slash_command(guild_ids=[guildID])
    async def vchannel_manage(self,interaction:Interaction):
        ## keep empty for subcommands
        pass


    ## voice channel create
    @vchannel_manage.subcommand(name="vchannel_create",description="Create a voicechannel for a category")
    async def vchannel_create(self,interaction:Interaction,voice_name:str,category_id:str):
        guild = interaction.guild
        category_id = int(category_id)
        vchannel_sel = guild.get_channel(category_id)

        await guild.create_voice_channel(name=voice_name,category=vchannel_sel)
        await interaction.response.send_message("Voicechannel create succesfully")


    ## voice channel delete
    @vchannel_manage.subcommand(name="vchannel_delete",description="Deletes a voicechannel for a category")
    async def vchannel_delete(self,interaction:Interaction,category_id:str):
        guild = interaction.guild
        category_id = int(category_id)
        vchannel_sel = guild.get_channel(category_id)

        await vchannel_sel.delete()
        await interaction.response.send_message("Voice channel deleted succesfully")
        


def setup(bot):
    bot.add_cog(Categories(bot))