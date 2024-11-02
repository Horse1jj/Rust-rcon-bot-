import discord

def create_embed(title, description):
    embed = discord.Embed(title=title, description=description, color=discord.Color.blue())
    return embed
