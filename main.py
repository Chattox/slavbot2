# Slavbot 2
# Slavic Guacamole

import sys
import asyncio
import discord
from discord import opus
import keys
import slavio as io
import slavsound
import slavfunc as func
import logging
import testtools as test
import shlex
import random

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

    while client.voice_clients:
        pass

    if msg.content.startswith("!"):
        # Figure out what command it is and print to stdout, also convert to lowercase for case-insensitivity
        cmd = msg.content[1:].split(" ")[0]
        args = shlex.split(msg.content)[1:]
        cmd = cmd.lower()
        print('COMMAND: %s' % (cmd))
        print('FROM: ' + msg.author.name)
        # Check if user has admin permission
        regUserList = await io.readUser(keys.regUsers)
        for i in regUserList:
            # print("Checking user: " + i.name)
            if i.id == msg.author.id:
                # print("ID match")
                if i.admin == True:
                    # print("Is admin")
                    isAdmin = True
                else:
                    # print("Is not admin")
                    isAdmin = False

        # SOUND COMMANDS
        # Load sound list from file for checking against command
        if isAdmin == True:
            sounds = await io.readFile(keys.soundList) + await io.readFile(keys.rSoundList)
        else:
            sounds = await io.readFile(keys.soundList)
        if cmd == "soundhelp": # Format sound list to PM to user
            await func.soundhelp(msg, isAdmin)
            await msg.delete()
        elif cmd in sounds: # Check if command is in the sound list
            await slavsound.playSound(msg, client)
            await msg.delete()
        elif cmd == "rand": # Play a random sound from the extended list
            randSound = await io.readFile(keys.soundList) + await io.readFile(keys.rSoundList)
            await slavsound.randSound(msg, client, randSound)
            await msg.delete()
        elif cmd == "randomaly": # Play a random anomaly sound
            randomalySound = await io.readFile(keys.anomalyList)
            await slavsound.randSound(msg, client, randomalySound)
            await msg.delete()

        # FUNCTION COMMANDS
        elif cmd == "dedmoroz":
            await func.dedmoroz(client)
            await msg.delete()
        elif cmd == "migrate":
            if isAdmin == True:
                await func.migrate(client, msg, args[0], args[1])
                await msg.delete()
            else:
                await msg.author.send("YOU'RE NOT MY REAL DAD")
                await msg.delete()



        # TEST TOOL COMMANDS
        elif cmd == "read":
            await test.readFileTest(args[0])
            await msg.delete()
        elif cmd == "voice":
            await test.voiceCheck(msg)
            await msg.delete()
        elif cmd == "readuser":
            await test.readUserTest(args[0])
        elif cmd == "testhelp":
            await test.testHelp(msg)
            await msg.delete()


        # UNRECOGNISED COMMAND
        else:
            await msg.author.send(msg.content + " is not a recognised command, урод.")
            await msg.delete()

        # END OF COMMANDS
        print("----------")

# Listen for people coming in and out of voice channels for log-in/out sounds
@client.event
async def on_voice_state_update(member, before, after):
    regUserList = await io.readUser(keys.regUsers)
    for i in regUserList:
        if member.id == i.id:
            # Check if user connected to valid channel (came from AFK or new join)
            was_disconnected = before.channel is None or before.afk is True
            is_connected = after.channel is not None and after.afk is False
            was_connect = was_disconnected and is_connected

            # Check if user disconnected
            was_connected = before.channel is not None and before.afk is False
            is_disconnected = after.channel is None and before.afk is False
            was_disconnect = was_connected and is_disconnected

            # If user connected to valid channel, play their join sound
            if was_connect:
                if i.name == "smord":
                    anomList = await io.readFile(keys.anomalyList)
                    snd = random.choice(anomList)
                    print(i.name + " joined, playing random Anomaly sound: " + snd)
                    await asyncio.sleep(1)
                    await slavsound.funcSound(after.channel, snd, client)
                if i.logIn != "none":
                    print(i.name + " joined, playing join sound: " + i.logIn)
                    await asyncio.sleep(1)
                    await slavsound.funcSound(after.channel, i.logIn, client)
                    print("----------")
                # else:
                #     print(i.name + " joined, but they do not have a join sound")
                #     print("----------")

            # If user disconnected from valid channel, play their leave sound
            if was_disconnect:
                if i.logOut != "none":
                    print(i.name + " left, playing leave sound: " + i.logOut)
                    await asyncio.sleep(2)
                    await slavsound.funcSound(before.channel, i.logOut, client)
                    print("----------")
                else:
                    print(i.name + " left, but they do not have a leave sound")
                    print("----------")



client.run(keys.client)