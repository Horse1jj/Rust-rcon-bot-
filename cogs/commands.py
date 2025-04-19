import discord
from discord.ext import commands
import json
from utils.rust import execute_rcon_command  

class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.servers = self.load_servers()

    def load_servers(self):
        with open("config/servers.json", "r") as f:
            return json.load(f)

    def get_server(self, server_name):
        return self.servers.get(server_name.lower())

    @commands.command(name="players", help="Displays the current players on the server.")
    async def players(self, ctx, server_name: str):
        server = self.get_server(server_name)
        if not server:
            await ctx.send(f"❌ Server `{server_name}` not found.")
            return

        command = "RefreshList" 
        response = execute_rcon_command(server, command)
        await ctx.send(f"**Players on `{server_name}`:**\n```\n{response}\n```")

    @commands.command(name="servers", help="Lists all available servers.")
    async def servers(self, ctx):
        server_list = [f"- {name}" for name in self.servers.keys()]
        await ctx.send("**Available servers:**\n" + "\n".join(server_list))

    @commands.command(name="serverinfo", help="Displays information about a specific server.")
    async def serverinfo(self, ctx, server_name: str):
        server = self.get_server(server_name)
        if not server:
            await ctx.send(f"❌ Server `{server_name}` not found.")
            return

        command = "ServerInfo"  
        response = execute_rcon_command(server, command)

        embed = discord.Embed(title=f"Server Info: {server_name}", color=discord.Color.blue())
        embed.add_field(name="IP", value=server["ip"], inline=True)
        embed.add_field(name="Port", value=server["port"], inline=True)
        embed.add_field(name="RCON", value="✅ Connected" if "Error" not in response else "❌ Error", inline=True)
        embed.add_field(name="Raw Response", value=f"```{response[:1000]}```", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(GeneralCommands(bot))
