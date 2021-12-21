import discord
from discord.ext import commands
from ...lib import ChannelAndMessageId


class BackUp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = "Create a backup for your server"
        self.backup_channel = 0

    @property
    def display_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="\U0001f4be")
    
    @commands.command(description="Create backup of the server")
    @commands.has_permissions(manage_guild=True)
    @commands.guild_only()
    @commands.cooldown(2,60,commands.BucketType.guild)
    async def backup(self):
        '''Create backup of the server'''
        pass

def setup(bot):
    bot.add_cog(BackUp(bot))