# Slavbot 2
# Slavic Guacamole

import sys
import discord
from discord import opus
import keys
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='slavbot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('On servers:')
    for s in client.guilds:
        print('- %s' % s.name)
    print('----------')
    if sys.maxsize > 2**32:
        print('Loading 64-bit opus...')
        opus.load_opus('./libopus-0.x64.dll')
        print('Loading complete')
    else:
        print('Loading 32-bit opus...')
        opus.load_opus('./libopus-0.x86.dll')
        print('Loading complete')
    print('----------')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

client.run(keys.client)