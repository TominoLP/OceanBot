import sys
import traceback
from abc import ABC

import discord
import time

from discord.ext import commands
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")
STARTUP = config_object["STARTUP"]

TOKEN = STARTUP["token"]
FLAGS = STARTUP["flags"]


class OceanBot(commands.Bot, ABC):
    initial_extensions = {"cogs.Commands"

                          }

    async def on_ready(self):
        print(f"############################## \n startup completed\n logged in as {self.user}")
        activity = discord.Game(name="/help", type=2)
        await bot.change_presence(status=discord.Status.online, activity=activity)


intents = discord.Intents.default()
bot = OceanBot(command_prefix=" ", help_command=None, intents=discord.Intents.all())

if __name__ == "__main__":
    for extension in bot.initial_extensions:
        try:
            bot.load_extension(extension)
            print(f"successful load: {extension}")
            time.sleep(0.5)
        except Exception as e:
            print(f"failed to load extension {extension}", file=sys.stderr)
            traceback.print_exc()

bot.run(TOKEN, reconnect=True)
