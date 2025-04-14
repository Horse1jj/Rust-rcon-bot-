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

class ModCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        # Check if the user has a moderator role
        return any(str(role.id) in roles["mod"] for role in ctx.author.roles)

    # Moderator commands
    @commands.command(name="mute", help="Mutes a player's in-game chat.")
    async def mute(self, ctx, player_name: str, server_name: str):
        server = servers.get(server_name)
        response = execute_rcon_command(server, f'admin.mutechat "{player_name}"')
        await ctx.send(embed=create_embed("Mute Player", f"Muted player {player_name} on server {server_name}. \nResponse: {response}"))

    @commands.command(name="unmute", help="Unmutes a player's in-game chat.")
    async def unmute(self, ctx, player_name: str, server_name: str):
        server = servers.get(server_name)
        response = execute_rcon_command(server, f'admin.unmutechat "{player_name}"')
        await ctx.send(embed=create_embed("Unmute Player", f"Unmuted player {player_name} on server {server_name}. \nResponse: {response}"))

def setup(bot):
    bot.add_cog(ModCommands(bot))
