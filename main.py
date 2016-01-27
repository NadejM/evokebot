import discord
import asyncio

import os

# load your key if existing
# move these to environ vars
# do rebase to remove from git history D:
PUBLIC_KEY = os.environ.get('__EVOKEPUBLIC__')
PRIVATE_KEY = os.environ.get('__EVOKEPRIVATE__')

# the existing regi

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    print(message.content.split())
    if message.content.startswith('!ilevel'):
        name = message.content.split()[1]
        await client.send_message(message.channel, name)

    elif message.content.startswith('!sleep'):
        await client.send_message(message.channel, 'Sleeping for 60 seconds, fuck you eve')
        await asyncio.sleep(60)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('dumb'):
        if message.author.name.startswith('Bobnamob'):
            await client.send_message(message.channel, 'I am a dumb bot :(')
        else:
            await client.send_message(message.channel, 'I only answer to Bobnamob!')

client.run('evokebot@gmail.com', 'bobnamob')