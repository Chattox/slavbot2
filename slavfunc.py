# Slav functions
# Extra stuff that doesn't deserve its own module

import random
import discord
import keys
import slavsound
import slavio as io

# Secret gibb with beard 2018
async def dedmoroz(client):
    # First get the message which people have reacted to. In this case I'm just using explicit IDs for the
    # channel and message because I'm lazy.
    channel = client.get_channel(keys.shamefur)
    message = await channel.get_message(keys.santaMsg)
    reaction = message.reactions
    memberList = list()

    # Now get the people who reacted to the message, and add them to the list of participants
    async for user in reaction[0].users():
        memberList.append(user)
    for member in memberList:
        print(member.name)
    # Randomly assign recipients
    random.shuffle(memberList)
    i = 0
    while i < len(memberList):
        await memberList[i].send("Welcome to Secret Slavbot 2018!\n"+
                                 "Your giftee this year is **" + memberList[(i + 1) % len(memberList)].name + "**!\n"+
                                 "The rules are:\n"+
                                 "1) Send your gift on the *second* day of the Steam Winter Sale. This allows people to look through the store for the perfect gift!\n"+
                                 "2) Don't spend more than £15, give or take £2.\n"+
                                 "3) Make sure to update your own Steam wishlist to make it easier for your gifter!\n"+
                                 "4) Don't tell anyone who you got in the raffle!")

        i+=1

# Command to migrate all members of one channel to another.
async def migrate(client, msg, origin, destination):
    before = discord.utils.get(msg.guild.voice_channels, name=origin)
    after = discord.utils.get(msg.guild.voice_channels, name=destination)
    try:
        print("Moving all members from \"%s\" to \"%s\"" % (before.name, after.name))
        await slavsound.funcSound(before, "leeroy", client)
        for user in before.members:
            await user.move_to(after)
    except AttributeError:
        await msg.author.send("One of the channels is not recognised!")

# Sound help: Actually Works™ edition
async def soundhelp(msg, isAdmin):
    sounds = await io.readFile(keys.soundList)
    if isAdmin:
        sounds = sounds + await io.readFile(keys.rSoundList)
    soundHelp = []
    soundHelpMsg = ""
    for i in sounds:
        soundHelp.append(i)
        soundHelpMsg = "\n\!".join(soundHelp)
        if len(soundHelpMsg) > 1800:
            await msg.author.send("\n\!"+soundHelpMsg)
            soundHelp.clear()
    await msg.author.send("\n\!"+soundHelpMsg)