import discord
from discord.ext import commands
from discord import app_commands
import json
import os

# Load configuration
with open("config.json") as config_file:
    config = json.load(config_file)

GUILD_ID = config.get("guild_id")  # Make sure it's an integer in your config


intents = discord.Intents.default()
intents.message_content = True
intents.members = True


class RustRconBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=config.get("prefix"), intents=intents)
        self.guild = discord.Object(id=GUILD_ID)  

    async def setup_hook(self):
        # Load all cogs
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")
        

        await self.tree.sync(guild=self.guild)

    async def on_ready(self):
        print(f'Logged in as {self.user.name} ({self.user.id})')
        print('------')

        with open("status.json") as status_file:
            status = json.load(status_file)
            activity = discord.Game(name=status.get("activity", "Default activity"))
            await self.change_presence(activity=activity)

bot = MyBot()

bot.run(config["token"])
