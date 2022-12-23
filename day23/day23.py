

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
        if grid[y-1][x-1] == "." and grid[y][x+1] == "." and grid[y+1][x+1] == ".": return True
        else: return False

def proposeAMove(elve):
    y,x, dir = elve["y"], elve["x"], elve["moveDir"]
    for i in range(dir, dir+4):
        if checkAvailabilityInDir(elve, i%4):
            elve["moveDir"] = i
            return True
        elve["moveDir"] = elve["moveDir"] +1
    return False

def elvesProposesMoves():
    for x in elves:
        if checkIfAnyElvesNearby(x):
            x["wtm"] = True
            if proposeAMove(x):x["propose"] = True
            else: x["propose"] = False
        else: 
            x["wtm"] = False
            continue
def getDestCoords(elve):
    y,x, dir = elve["y"], elve["x"], elve["moveDir"]
    if dir%4 == 0: return [y-1,x]
    if dir%4 == 1: return [y+1,x]
    if dir%4 == 2: return [y,x-1]
    if dir%4 == 3: return [y,x+1]

def checkifSpotAlreadyTaken(coords):
    if grid[coords[0]][coords[1]] != ".":
        print("elves to same spot:", coords)
        return True
    else: return False

#moveDir: 0-N, 1-South, 2-West, 3 - East
def movePrevElveBack(coords): 
    for elve in elves:
        if elve["y"] == coords[0] and elve["x"] == coords[1]:
            y,x,dir = elve["y"], elve["x"], elve["moveDir"]
            if dir%4 == 0:  makeAMove(elve, [y+1,x] )#elve["y"] = elve["y"] +1
            elif dir%4 == 1: elve["y"] = elve["y"] -1
            elif dir%4 == 2: elve["x"] = elve["x"] +1
            elif dir%4 == 3: elve["x"] = elve["x"] -1 
            break

def makeAMove(elve,coords):
    grid[elve["y"]][elve["x"]] = "."
    elve["y"], elve["x"] = coords[0], coords[1]
    grid[coords[0]][coords[1]] = "#"

def elvesMove():
    for x in elves:
        destCoords = getDestCoords(x)
        if checkifSpotAlreadyTaken(destCoords):
            movePrevElveBack(destCoords)
        else:
            makeAMove(x,destCoords)

f = open("day23/day23.txt")
grid = []
extra = 0 #Extra empty cells to add everywhere
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
            elves.append({"no":cnt, "y": i,"x":j,"wtm":False,"moveDir":0})

rounds = 10

for i in range(0,1):
    elvesProposesMoves()
    elvesMove()

for x in grid:
    print("".join(x))

# for i in range(7,len(grid)-7):
#     #print(x)
#     print("".join(grid[i]))
