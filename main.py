import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print(f'Now login as: {bot.user}')
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('Hi'):
        tmp = message.content.split(' ', 1)
        if len(tmp) == 1:
            await message.channel.send(f'{message.author.mention} 請問你要說什麼？')
        else:
            await message.channel.send(f'{message.author.mention} 說了 「{tmp[1]}」')

# @bot.event
# async def on_member_join(member):
#     await member.channel.send(f'Welcome to 開源星手村, {member}')

if __name__ == '__main__':
    bot.run(os.getenv('TOKEN'))