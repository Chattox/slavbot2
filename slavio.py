import regularids as regs

# Read file, return list
async def readFile(file):
    fileList = []
    with open(file, "r") as f:
        for line in f.readlines():
            if not line.startswith('#'):
                line = line.replace("\n","")
                fileList.append(line)
    return(fileList)

# Read file, parse data into regular() instances
async def readUser(file):
    userList = []
    with open(file, "r") as f:
        for line in f.readlines():
            if not line.startswith('#'):
                lineData = line.split("=")
                print(lineData[0] + " " + lineData[1])