import discord

from discord.ext import commands
from discord.commands import slash_command


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[881207955029110855])
    async def hello(ctx):
        await ctx.respond("Hello!")


def setup(bot):
    bot.add_cog(Commands(bot))
