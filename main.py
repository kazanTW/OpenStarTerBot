import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print(f'Now login as: {bot.user}')

for FileName in os.listdir('./cmds'):
    if FileName.endswith('.py'):
        bot.load_extension(f'cmds.{FileName[:-3]}')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reloaded')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded')

# @bot.event
# async def on_member_join(member):
#     await member.channel.send(f'Welcome to 開源星手村, {member}')

if __name__ == '__main__':
    bot.run(os.getenv('TOKEN'))