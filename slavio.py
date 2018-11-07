
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
class regular():
    name = ""
    id = 0
    logIn = ""
    logOut = ""
    admin = False

async def readUser(file):
    with open(file, "r") as f:
        userList = list()
        userNum = 0
        regName = ""
        regID = ""
        regIn = ""
        regOut = ""
        regAdmin = False
        for line in f.readlines():
            line = line.strip('\n')
            if not line.startswith('#'):
                lineData = line.split("=")
                if lineData[0] == "name":
                    regName = lineData[1]
                if lineData[0] == "id":
                    regID = int(lineData[1])
                if lineData[0] == "logIn":
                    if lineData[1] == "none":
                        regIn = "none"
                    else:
                        regIn = lineData[1]
                if lineData[0] == "logOut":
                    if lineData[1] == "none":
                        regOut = "none"
                    else:
                        regOut = lineData[1]
                if lineData[0] == "admin":
                    if lineData[1] == "True":
                        regAdmin = True
                    else:
                        regAdmin = False
            if line.startswith('-'):
                userList.append(regular())
                userList[userNum].name = regName
                userList[userNum].id = regID
                userList[userNum].logIn = regIn
                userList[userNum].logOut = regOut
                userList[userNum].admin = regAdmin
                userNum+=1
        return userList