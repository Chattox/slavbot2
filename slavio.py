# Read file, return list
async def readFile(file):
    fileList = []
    with open(file, "r") as f:
        for line in f.readlines():
            if not line.startswith('#'):
                line = line.replace("\n","")
                fileList.append(line)
    return(fileList)