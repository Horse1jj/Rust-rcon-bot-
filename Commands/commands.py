import discord
from discord.ext import commands

class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="players", help="Displays the current players on the server.")
    async def players(self, ctx, server_name: str):
        # Logic to get players would go here
        await ctx.send(f"Displaying players on server {server_name}.")

    @commands.command(name="servers", help="Lists all available servers.")
    async def servers(self, ctx):
        # Logic to list servers would go here
        await ctx.send("Available servers: rust1, rust2.")

    @commands.command(name="serverinfo", help="Displays information about a specific server.")
    async def serverinfo(self, ctx, server_name: str):
        # Logic to get server info would go here
        await ctx.send(f"Displaying info for server {server_name}.")

def setup(bot):
    bot.add_cog(GeneralCommands(bot))
