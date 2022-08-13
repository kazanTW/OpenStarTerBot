import discord
client = discord.Client()

@client.event
async def on_ready():
    print(f'Now login as: {client.user}')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Hi'):
        tmp = message.content.split(' ', 1)
        if len(tmp) == 1:
            await message.channel.send(f'{message.author.mention} 請問你要說什麼？')
        else:
            await message.channel.send(f'{message.author.mention} 說了 「{tmp[1]}」')

# @client.event
# async def on_member_join(member):
#     await member.channel.send(f'Welcome to 開源星手村, {member}')

if __name__ == '__main__':
    TOKEN = open('token.txt').readline()
    client.run(TOKEN)