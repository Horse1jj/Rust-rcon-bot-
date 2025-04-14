import discord
from discord.ext import commands
from utils.rcon_utils import execute_rcon_command
from utils.embed_utils import create_embed
import json

# Load server and role configurations
with open("servers.json") as f:
    servers = json.load(f)
with open("roles.json") as f:
    roles = json.load(f)

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        # Check if the user has an admin role
        return any(str(role.id) in roles["admin"] for role in ctx.author.roles)

    # Admin commands
    @commands.command(name="giveitem", help="Gives an item to a player.")
    async def give_item(self, ctx, player_name: str, item_name: str, server_name: str):
        server = servers.get(server_name)
        response = execute_rcon_command(server, f'give "{player_name}" "{item_name}"')
        await ctx.send(embed=create_embed("Give Item", f"Gave {item_name} to {player_name} on server {server_name}. \nResponse: {response}"))

    @commands.command(name="kick", help="Kicks a player from the server.")
    async def kick_player(self, ctx, player_name: str, server_name: str):
        server = servers.get(server_name)
        response = execute_rcon_command(server, f'kick "{player_name}"')
        await ctx.send(embed=create_embed("Kick Player", f"Kicked {player_name} from server {server_name}. \nResponse: {response}"))

    @commands.command(name="ban", help="Bans a player from the server.")
    async def ban_player(self, ctx, player_name: str, server_name: str):
        server = servers.get(server_name)
        response = execute_rcon_command(server, f'ban "{player_name}"')
        await ctx.send(embed=create_embed("Ban Player", f"Banned {player_name} from server {server_name}. \nResponse: {response}"))

    @commands.command(name="mutechat", help="Mutes a player in-game.")
    async def mute_chat(self, ctx, player_name: str, server_name: str):
        server = servers.get(server_name)
        response = execute_rcon_command(server, f'admin.mutechat "{player_name}"')
        await ctx.send(embed=create_embed("Mute Chat", f"Muted {player_name} on server {server_name}. \nResponse: {response}"))

    @commands.command(name="unmutechat", help="Unmutes a player in-game.")
    async def unmute_chat(self, ctx, player_name: str, server_name: str):
        server = servers.get(server_name)
        response = execute_rcon_command(server, f'admin.unmutechat "{player_name}"')
        await ctx.send(embed=create_embed("Unmute Chat", f"Unmuted {player_name} on server {server_name}. \nResponse: {response}"))

    @commands.command(name="quit", help="Saves everything and stops the server.")
    async def quit_server(self, ctx):
        server = servers.get("rust1")  # Default server, adjust as needed
        response = execute_rcon_command(server, "quit")
        await ctx.send(embed=create_embed("Quit Server", response))

    # Weather commands
    @commands.command(name="weather.fog", help="Sets fog weather.")
    async def set_fog(self, ctx):
        server = servers.get("rust1")  # Default server, adjust as needed
        response = execute_rcon_command(server, "weather.fog()")
        await ctx.send(embed=create_embed("Set Weather Fog", response))

    @commands.command(name="weather.wind", help="Sets wind weather.")
    async def set_wind(self, ctx):
        server = servers.get("rust1")  # Default server, adjust as needed
        response = execute_rcon_command(server, "weather.wind()")
        await ctx.send(embed=create_embed("Set Weather Wind", response))

    @commands.command(name="weather.rain", help="Sets rain weather.")
    async def set_rain(self, ctx, value: str):
        server = servers.get("rust1")  # Default server, adjust as needed
        response = execute_rcon_command(server, f"weather.rain {value}")
        await ctx.send(embed=create_embed("Set Weather Rain", response))

def setup(bot):
    bot.add_cog(AdminCommands(bot))
