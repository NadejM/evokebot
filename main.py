#! /usr/bin/env python
import discord
import asyncio
import handle

import os

client = discord.Client()

PASSWORD = os.environ.get('EVOKEBOT_PASSWORD')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    print(message.content.split())
    #Remove this once testing complete.
    if message.channel.name == "bot_testing":
        if message.content.startswith('!ilevel'):
            out_message = handle.ilevel(message)
            await client.send_message(message.channel, out_message)

        if message.content.startswith('!achieve'):
            out_message = handle.achieve(message)
            await client.send_message(message.channel, out_message)

        elif message.content.startswith('!sleep'):
            await client.send_message(message.channel, 'Sleeping for 60 seconds. Wake me up when Gorefiend is dead.')
            await asyncio.sleep(120)
            await client.send_message(message.channel, 'Done sleeping')

        elif message.content.startswith('!links'):
            out_message = handle.links(message)
            await client.send_message(message.channel, out_message)

        elif message.author.name.startswith('Bobnamob'):
            if message.content.startswith('dumb'):
                await client.send_message(message.channel, 'I am a dumb bot :(')
            elif message.content.startswith('!stats'):
                await client.send_message(message.channel, 'Placeholder for bot stats. (Uptime, messages sent, etc...)')

client.run('evokebot@gmail.com', PASSWORD)
