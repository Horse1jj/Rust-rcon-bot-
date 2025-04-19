import discord
from discord.ext import commands
from utils.embed import create_embed

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", help="Displays available commands.")
    async def help_command(self, ctx):
        embed = create_embed("Help", "Here are the available commands:")

        # Iterate over cogs and list commands in each
        for cog_name, cog in self.bot.cogs.items():
            commands_list = cog.get_commands()
            if commands_list:
                command_names = [command.name for command in commands_list]
                embed.add_field(name=cog_name.capitalize(), value=", ".join(command_names), inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
