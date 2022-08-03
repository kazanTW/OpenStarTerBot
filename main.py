import discord
client = discord.Client()

@client.event
async def on_ready():
    print(f'Now login as: {client.user}')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'Hi':
        await message.channel.send('Hello!')

# @client.event
# async def on_member_join(member):
#     await member.channel.send(f'Welcome to 開源星手村, {member}')

if __name__ == '__main__':
    client.run('TOKEN')