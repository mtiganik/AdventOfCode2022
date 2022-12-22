def changeDir(cmd,current):
    if current == "U":
        if cmd =="R": return "R"
        if cmd == "L": return "L"
    if current == "R":
        if cmd == "R": return "D"
        if cmd == "L": return "U"
    if current == "D":
        if cmd == "R": return "L"
        if cmd == "L": return "R"
    if current == "L":
        if cmd == "R": return "U"
        if cmd == "L": return "D"


f = open("day22/day22.txt")
grid = []
cmdList = ""
maxlen = 0
for x in f:
    if len(x) > 2:
        if len(x) > maxlen:
            maxlen = len(x)
        grid.append(list(x.rstrip()))
    else:
        cmdList = "R" + f.readline()
cmdList = cmdList.replace("L"," L").replace("R"," R").strip()
cmdList = cmdList.split(" ")
coords = [0,grid[0].index("."), "U"]
        
for i,x in enumerate(grid):
    if len(grid[i])< maxlen:
        grid[i] = grid[i] + [" "]*(maxlen-len(grid[i]))

def getCoords(curCoords):
    dir = curCoords[2]
    newCoords = [curCoords[0], curCoords[1], dir]
    if dir == "U": newCoords[0] = newCoords[0] -1
    if dir == "R": newCoords[1] = newCoords[1] +1
    if dir == "D": newCoords[0] = newCoords[0] +1
    if dir == "L": newCoords[1] = newCoords[1] -1
    return newCoords

def checkCoordsOutside(coords):
    if coords[0] == -1 or coords[0] == len(grid) or coords[1] == -1 or coords[1] == len(grid[0]): return True
    else: return False

def getCoordsOtherSide(currCoords):
    dir = currCoords[2]
    col,row = currCoords[0], currCoords[1] 
    newCoords = [currCoords[0], currCoords[1], dir]
    if dir == "U":
        for i in range(len(grid)-1,0,-1):
            if grid[i][row] == "." or grid[i][row] == "#": return [i,row,dir]
    if dir == "R":
        for i in range(0,len(grid[0])):
            if grid[col][i] == "." or grid[col][i] == "#": return [col,i,dir]
    if dir == "D":
        for i in range(0,len(grid)):
            if grid[i][row] == "." or grid[i][row] == "#": return [i,row,dir]
    if dir == "L":
        for i in range(len(grid[0])-1,0,-1):
            if grid[col][i] == "." or grid[col][i] == "#": return [col,i,dir]




def move(cmd):
    dir = changeDir(cmd[0], coords[2])
    moves = int(cmd[1:])
    curCoords = coords
    curCoords[2] = dir
    for k in range(0,moves):
        nc = getCoords(curCoords)
        if checkCoordsOutside(nc):
            newCoords = getCoordsOtherSide(nc)
            if(grid[newCoords[0]][newCoords[1]])== "#": break
            else: curCoords = newCoords
        elif (grid[nc[0]][nc[1]]) == " ":
            newCoords = getCoordsOtherSide(nc)
            if(grid[newCoords[0]][newCoords[1]])== "#": break
            else: curCoords = newCoords
        elif(grid[nc[0]][nc[1]]) == ".":
            curCoords = nc
        elif (grid[nc[0]][nc[1]]) == "#":
            break
    return curCoords

def printGrid():
    for x in grid:
        print("".join(x))

for i,x in enumerate(cmdList):
    coords = move(x)
    # grid[coords[0]][coords[1]] = str(i)
    # print("after move",i)
    # printGrid()


def facingVal(dir):
    if dir == "R": return 0
    if dir == "D": return 1
    if dir == "L": return 2
    if dir == "U": return 3

sum = (coords[0]+1)*1000 + (coords[1] +1)*4 + facingVal(coords[2])
print("end sum:", sum)