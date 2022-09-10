import discord
from discord.ext import commands
import os
from core import Cog_Extension

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.content.startswith('Hi'):
            tmp = message.content.split(' ', 1)
            if len(tmp) == 1:
                await message.channel.send(f'{message.author.mention} 請問你要說什麼？')
            else:
                await message.channel.send(f'{message.author.mention} 說了 「{tmp[1]}」')

def setup(bot):
    bot.add_cog(Event(bot))