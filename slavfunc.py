# Slav functions
# Extra stuff that doesn't deserve its own module

import random

# Secret gibb with beard
async def dedmoroz(file):
    # Load participants into a list from file
    memberList = list()
    with open(file, "r") as f:
        for line in f.readlines():
            line = line.strip('\n')
            memberList.append(line)
    # Randomly assign gifter/giftee pairs
    random.shuffle(memberList)
    i = 0
    while i < len(memberList):
        print(memberList[i] + " gets " + memberList[(i+1)%len(memberList)])
        i+=1