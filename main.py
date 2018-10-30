# Slavbot 2
# Slavic Guacamole

import sys
import discord
from discord import opus
import keys
#import slavsound
import logging

# Create logger, output log to file
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='slavbot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

# Start up, load opus version based on 32/64bit
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

# Listen for commands
@client.event
async def on_message(msg):
    # If message is from slavbot, ignore
    if msg.author == client.user:
        return

    if msg.content.startswith("!"):
        # Figure out what command it is and print to stdout, also convert to lowercase for case-insensitivity
        cmd = msg.content[1:].split(" ")[0]
        args = msg.content.split(" ")[1:]
        cmd = cmd.lower()
        print('COMMAND: %s' % (cmd))
        print('FROM: ' + msg.author.name)

client.run(keys.client)