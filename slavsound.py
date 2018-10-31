# Sound module
# Play specific sounds on command, as well as when specific users join/leave channels. Also random function.

import discord
import random
import keys
import slavio as io

# Play specific sound on command
async def playSound(self, sound):
    if sound.author.voice: # Check user is in voice channel
        try:
            snd = sound.content[1:].split(" ")[0]