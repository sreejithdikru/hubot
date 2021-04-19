import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '.')

@client.event
async def on_member_join(ctx, *, member):
    channel = member.server.get_channel("channel id")
    fmt = 'Welcome to the {1.name} Discord server, {0.mention}'
    await ctx.send_message(channel, fmt.format(member, member.server))

@client.event
async def on_member_remove(ctx, *, member):
    channel = member.server.get_channel("channel id")
    fmt = '{0.mention} has left/been kicked from the server.'
    await ctx.send_message(channel, fmt.format(member, member.server))

client.run('client id')