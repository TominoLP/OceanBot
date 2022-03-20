from discord.commands import slash_command
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[955091724689088512])
    async def hello(self, ctx):
        await ctx.respond("Hello!")


def setup(bot):
    bot.add_cog(Commands(bot))
