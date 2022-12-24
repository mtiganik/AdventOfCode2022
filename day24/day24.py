f = open("day24/day24.txt")
grid = []
for x in f:
    grid.append(list(x.rstrip()))
winds = []
cnt = 0
def getWind(char):
    if char == ">": return ">"
    elif char == "<": return "<"
    elif char == "v": return "v"
    elif char == "^": return "^"
    else: return 0
for i,x in enumerate(grid):
    for j,k in enumerate(x):
        wind = getWind(k)
        if wind !=0:
            winds.append({"d":wind,"y": i,"x":j})

def getNewCoords(y,x,d):
    if d == "v":
        if y < len(grid) -2:
            return [y +1,x]
        else: return [1,x]
    if d == ">":
        if x < len(grid[0])-2:
            return [y,x+1]
        else: return [y,1]
    if d == "^":
        if y > 2:
            return [y-1,x]
        else: return [len(grid)-2,x]
    if d == "<":
        if x > 2:
            return [y,x-1]
        else: return[y, len(grid[0])-2] 
        
def writeGrid(oldCoords,newCoords,d):
    oldchar, newChar = grid[oldCoords[0]][oldCoords[1]], grid[newCoords[0]][newCoords[1]]
    if oldchar.isdigit():
        if oldchar == "1": grid[oldCoords[0]][oldCoords[1]] = "."
        else:
            olddigit = int(oldchar) -1
            grid[oldCoords[0]][oldCoords[1]] =  str(olddigit)
    else: grid[oldCoords[0]][oldCoords[1]] = "."
    if newChar == ".":
        grid[newCoords[0]][newCoords[1]] = d
    else:
        if newChar.isdigit():
            newChar = int(newChar) +1
            grid[newCoords[0]][newCoords[1]] =str(d)
        else: grid[newCoords[0]][newCoords[1]] = "2"

def writeGrid(nc,oc,nchar,ochar):
    grid[nc[0]][nc[1]]= nchar
    grid[oc[0]][oc[1]] = ochar

def changeWind(wind):
    y,x,d = wind["y"], wind["x"],wind["d"]
    [ny,nx] = getNewCoords(y,x,d)
    if grid[y,x] != "M"
    writeGrid([y,x],[ny,nx],d)
    wind["y"], wind["x"] = ny,nx

def printGrid():
    print("")
    for x in grid:
        print("".join(x))
def moveWinds():
    for i,x in enumerate(winds):
        changeWind(x)

for i in range(0,2):
    moveWinds()
    printGrid()

