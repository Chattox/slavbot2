# Slavbot 2
# Slavic Guacamole

import sys
import discord
from discord import opus
import keys
import slavio as io
#import slavsound
import logging
import testtools as test

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

        # SOUND COMMANDS
        # Load sound list from file for checking against command
        sounds = await io.readFile(keys.soundList)
        if cmd == "soundhelp": # Format sound list to PM to user
            soundHelp = "\n\!".join(sounds)
            await msg.author.send("Opaaa, have some sound commands: \n\!"+soundHelp)
        if cmd in sounds: # Check if command is in the sound list
            await soundboard.playSound(msg)


        # TEST TOOL COMMANDS
        if cmd == "read":
            await test.readFileTest(args[0])
        if cmd == "voice":
            await test.voiceCheck(msg)

client.run(keys.client)