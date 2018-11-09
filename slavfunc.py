# Slav functions
# Extra stuff that doesn't deserve its own module

import random
import discord
import keys

# Secret gibb with beard
# async def dedmoroz(file):
#     # Load participants into a list from file
#     memberList = list()
#     with open(file, "r") as f:
#         if not line.startswith('#'):
#             for line in f.readlines():
#                 line = line.strip('\n')
#                 memberList.append(line)
#     # Randomly assign gifter/giftee pairs
#     random.shuffle(memberList)
#     i = 0
#     while i < len(memberList):
#         print(memberList[i] + " gets " + memberList[(i+1)%len(memberList)])
#         i+=1

async def dedmoroz(client):
    # First get the message which people have reacted to. In this case I'm just using explicit IDs because
    # I'm lazy.
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
        print(memberList[i].name + " gets " + memberList[(i+1)%len(memberList)].name)
        i+=1