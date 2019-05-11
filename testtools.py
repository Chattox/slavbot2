# Commands/functions for testing stuff in slavbot
import slavio as io
import keys

async def readFileTest(file):
    fileContents = await io.readFile(file)
    print(fileContents)

# Check if user is in a voice channel
async def voiceCheck(msg):
    if msg.author.voice:
        print("User is in voice channel: " + msg.author.voice.channel.name)
    else:
        print("User is not in voice channel")

# Test user reading function
async def readUserTest(file):
    await io.readUser(file)

# Lets fix this damn help command
async def testHelp(msg):
    sounds = await io.readFile(keys.soundList)
    testSoundHelp = []
    soundHelpMsg = ""
    for i in sounds:
        testSoundHelp.append(i)
        soundHelpMsg = "\n\!".join(testSoundHelp)
        if len(soundHelpMsg) > 1800:
            await msg.author.send("\n\!"+soundHelpMsg)
            testSoundHelp.clear()
    await msg.author.send("\n\!"+soundHelpMsg)