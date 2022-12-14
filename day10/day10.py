
def writeGrid():
    global spritePos, outGrid, cycle, currRow
    if spritePos[cycle -1] == "#":
        outGrid[currRow].append("#")
    else:
        outGrid[currRow].append(".")

def changeSprite(spritePos, X):
    newSprite = ["."]*41
    newSprite[X-1] = "#"
    newSprite[X] = "#"
    newSprite[X+1] = "#"
    return newSprite

f = open("day10.txt")

spritePos = "###....................................."
spritePos = list(spritePos)

outGrid = [[]]
currRow = 0
cycle = 1
X = 1
for x in f:
    if "noop" in x:
        writeGrid()
        cycle = cycle +1
    else:
        writeGrid()
        cycle = cycle +1
        if (cycle-1)%40 == 0:
            print("cycle changed at ", x)
            cycle = 1
            currRow = currRow +1
            outGrid.append([])

        writeGrid()
        val = int(x.split()[1])
        X = X + val
        spritePos = changeSprite(spritePos, X)
        cycle = cycle +1
    if (cycle-1)%40 == 0:
        print("cycle changed at ", x)
        cycle = 1
        currRow = currRow +1
        outGrid.append([])


sum = 0


for x in outGrid:
    str = ""
    str = str.join(x)
    print(str)
