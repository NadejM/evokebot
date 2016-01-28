import discord
import asyncio
import bnet

import os

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
        realm = message.content.split()[2]
        ilevel = bnet.ilevelReq(realm, name)
        out_message = name + "-" + realm + " has an average equipped ilevel of " + str(ilevel)
        await client.send_message(message.channel, out_message)

    if message.content.startswith('!achieve'):
        name = message.content.split()[1]
        realm = message.content.split()[2]
        points = bnet.achievementReq(realm, name)
        out_message = name + "-" + realm + " has " + str(points) + " achievement points."
        await client.send_message(message.channel, out_message)

    elif message.content.startswith('!sleep'):
        await client.send_message(message.channel, 'Sleeping for 60 seconds, fuck you eve')
        await asyncio.sleep(60)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.author.name.startswith('Bobnamob'):
        if message.content.startswith('dumb'):
            await client.send_message(message.channel, 'I am a dumb bot :(')
        elif message.content.startswith('!stats'):
            await client.send_message(message.channel, 'Placeholder for bot stats. (Uptime, messages sent, etc...)')

client.run('evokebot@gmail.com', 'bobnamob')
