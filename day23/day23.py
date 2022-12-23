def checkIfAnyElvesNearby(elve):
    y,x =elve["y"], elve["x"]
    if grid[y-1][x-1] == "." and grid[y-1][x]=="." and grid[y-1][x+1]=="." and grid[y][x-1] == "." and grid[y][x+1]=="." and grid[y+1][x-1] == "." and grid[y+1][x]=="." and grid[y+1][x+1]== ".":
        return False
    else: return True

def checkAvailabilityInDir(elve, dirToCheck):
    y,x = elve["y"], elve["x"]
    if dirToCheck == 0:
        if grid[y-1][x-1] == "." and grid[y-1][x] == "." and grid[y-1][x+1]==".": return True
        else: return False
    if dirToCheck == 1:
        if grid[y+1][x-1] == "." and grid[y+1][x] == "." and grid[y+1][x+1]==".": return True
        else: return False
    if dirToCheck == 2:
        if grid[y-1][x-1] == "." and grid[y][x-1] == "." and grid[y+1][x-1] == ".": return True
        else: return False
    if dirToCheck == 3:
        if grid[y-1][x+1] == "." and grid[y][x+1] == "." and grid[y+1][x+1] == ".": return True
        else: return False

def proposeAMove(elve):
    y,x, dir = elve["y"], elve["x"], elve["moveDir"]
    for i in range(0, 4):
        if checkAvailabilityInDir(elve, (dir + i)%4):
            elve["moveDir"] = dir + i
            return True
    return False

def elvesProposesMoves():
    moveOccured = False
    for x in elves:
        if checkIfAnyElvesNearby(x):
            moveOccured = True
            x["moveDir"] = direction
            if proposeAMove(x): x["wtm"] = True
            else: x["wtm"] = False
        else: 
            x["wtm"] = False
            continue
    return moveOccured

def getDestCoords(elve):
    y,x, dir = elve["y"], elve["x"], elve["moveDir"]
    if dir%4 == 0: return [y-1,x]
    if dir%4 == 1: return [y+1,x]
    if dir%4 == 2: return [y,x-1]
    if dir%4 == 3: return [y,x+1]

def checkifSpotAlreadyTaken(coords):
    if grid[coords[0]][coords[1]] != ".":
        return True
    else: return False

def movePrevElveBack(coords): 
    for elve in elves:
        if elve["y"] == coords[0] and elve["x"] == coords[1]:
            y,x,dir = elve["y"], elve["x"], elve["moveDir"]
            if dir%4 == 0:  makeAMove(elve, [y+1,x] )
            elif dir%4 == 1: makeAMove(elve, [y-1,x])
            elif dir%4 == 2: makeAMove(elve, [y,x+1])
            elif dir%4 == 3: makeAMove(elve, [y,x-1]) 
            break

def makeAMove(elve,coords):
    grid[elve["y"]][elve["x"]] = "."
    elve["y"], elve["x"] = coords[0], coords[1]
    grid[coords[0]][coords[1]] = "#"

def elvesMove():
    for x in elves:
        if x["wtm"] == True:
            destCoords = getDestCoords(x)
            if checkifSpotAlreadyTaken(destCoords):
                movePrevElveBack(destCoords)
            else:
                makeAMove(x,destCoords)

#Part 1
extra = 10 #not more than that needed

#Part 2
extra = 60 #need more empty cells everywhere

f = open("day23/day23.txt")
grid = []
for x in f:
    x = "."*extra + x.rstrip() + "."*extra
    grid.append(list(x))
for i in range(0,extra):
    grid.insert(0,["."]*len(grid[0]))
    grid.append(["."]*len(grid[0]))
elves = []
cnt = 0
for i,x in enumerate(grid):
    for j,k in enumerate(x):
        if k == "#":
            cnt = cnt+1
            elves.append({"y": i,"x":j,"wtm":False,"moveDir":3})

moveOccured = False

#Part 1:  
################# for part 2 delete this and uncommet part2 stuff
direction = 0
for i in range(0,10):
    elvesProposesMoves()
    elvesMove()
    direction = (direction + 1)%4

while True:
        if "#" not in grid[0]:
            grid.pop(0)
        elif "#" not in grid[len(grid)-1]:
            grid.pop()
        else: break
def removeFirstRows():
    while True:
        for j in range(0,len(grid)):
            if grid[j][0] == "#": return 0
        for j in range(0,len(grid)):
            grid[j].pop(0)
def removeLastRows():
    for i in range(len(grid[0])-1,0,-1):
        for j in range(0, len(grid)):
            if grid[j][i] == "#": return 0
        for j in range(0,len(grid)):
            grid[j].pop()
removeFirstRows()
removeLastRows()

cnt = 0
for i,x in enumerate(grid):
    for k in x:
        if k == ".": cnt = cnt +1
print("Part1:", cnt)


#Part 2:
#################
# direction = 0
# moveOccured = True
# movesCnt = 0
# while moveOccured == True:
#     movesCnt = movesCnt +1
#     if elvesProposesMoves() == False: break
#     elvesMove()
#     direction = (direction + 1)%4

# print("Part2", movesCnt)