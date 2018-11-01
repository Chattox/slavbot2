# Sound module
# Play specific sounds on command, as well as when specific users join/leave channels. Also random function.

import discord
import random
import keys
import regularids as reg
import slavio as io

# Play specific sound on command
async def playSound(sound):
    if sound.author.voice: # Check user is in voice channel
        snd = sound.content[1:].split(" ")[0]
        print("Playing: " + snd + ".mp3")
        print("Connecting to: " + sound.author.voice.channel.name)
        vc = await sound.author.voice.channel.connect()
        print("Playing...")
        vc.play(discord.FFmpegPCMAudio("./sounds/" + snd + ".mp3"))
        while vc.is_playing():
            pass
        await vc.disconnect()
        print("Done.")
    else:
        await sound.channel.send(sound.author.name + ", you're not in a voice channel, блядь!")

# Play random sound, including the lEgEnDaRy SoUnDs!
async def randSound(msg):
    if msg.author.voice: # Check user is in voice channel
        sounds = await io.readFile(keys.soundList)
        rSounds = await io.readFile(keys.rSoundList)
        soundList = sounds + rSounds # Compile a list of both regular sounds and random-only sounds to pick from
        snd = random.choice(soundList) # Pick a sound at random from this list
        print("Playing random sound: " + snd + ".mp3")
        print("Connecting to: " + msg.author.voice.channel.name)
        vc = await msg.author.voice.channel.connect()
        print("Playing...")
        vc.play(discord.FFmpegPCMAudio("./sounds/" + snd + ".mp3"))
        while vc.is_playing():
            pass
        await vc.disconnect()
        print("Done.")
    else:
        await msg.channel.send(msg.author.name + ", you're not in a voice channel, блядь!")