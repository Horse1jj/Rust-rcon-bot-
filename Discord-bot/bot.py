import discord
from discord.ext import commands
import json
import os

# Load configuration settings
with open("config.json") as config_file:
    config = json.load(config_file)

# Set up intents (required for certain events)
intents = discord.Intents.default()
intents.members = True  
intents.message_content = True

# Create bot instance with command prefix
bot = commands.Bot(command_prefix=config.get("prefix"), intents=intents)

# Load all cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

# Event to indicate bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')
    
    # Optionally set bot status
    with open("status.json") as status_file:
        status = json.load(status_file)
        activity = discord.Game(name=status.get("activity", "Default activity"))
        await bot.change_presence(activity=activity)

# Error handling for command errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("That command does not exist. Type `{config.prefix}help` for a list of commands.")
    else:
        await ctx.send(f"An error occurred: {error}")

# Run the bot
bot.run(config["token"])

