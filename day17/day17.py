

shapes = [[["@","@","@","@"]],
        [[".","@","."],
        ["@","@","@"],
        [".","@","."]],
        [[".",".","@"],
        [".",".","@"],
        ["@","@","@"]],
        [["@"],
        ["@"],
        ["@"],
        ["@"]],
        [["@","@"],
        ["@","@"]]]
def initializeGrid(s):
    for i in range(0,len(s)+3):
        if i < len(s):
            colToAdd = ""
            for j in range(0,7):
                if j <2:
                    colToAdd = colToAdd + "."
                elif j < 2+len(s[0]):
                    colToAdd = colToAdd + s[i][j-2]
                else: colToAdd = colToAdd + "."
            grid.insert(i,colToAdd)
        else: grid.insert(i,".......")

def getShapeStringCoords():
    s,e = -1,0
    startSet = False
    for i,x in enumerate(grid):
        if "@" in x and not startSet:
            s = i
            startSet = True
        if not "@" in x and s > -1:
            e = i
            break
    return [s,e]   

def checkLRCollision(p):
    [start,end] = getShapeStringCoords()
    for i in range(start,end):
        for j in range(0,7):
            try:
                if p == ">":
                    if grid[i][j] == "@":
                        if grid[i][j+1] ==".":break
                        elif grid[i][j+1] == "#": return True
                if p == "<":
                    if grid[i][j] == "@":
                        if j == 0: return True
                        elif grid[i][j-1] == ".":break
                        elif grid[i][j-1] == "#": return True
            except IndexError:
                return True
    return False
def checkDownMvnt():
    [start,end] = getShapeStringCoords()
    for i in range(start, end):
        for j in range(0,7):
            try:
                if grid[i][j] == "@" and grid[i+1][j] == "#":
                    return False
            except IndexError:
                return False
    return True

def moveRight():
    [start,end] = getShapeStringCoords()
    for i in range(start,end):
        for j in range(6,-1,-1):
            if grid[i][j] == "@":
                grid[i] = grid[i][:j] + "." +grid[i][j+1:]
                grid[i] = grid[i][:j+1] + "@"+grid[i][j+2:]
def printBoard():
    for x in grid:
        print(x)

def moveLeft():
    [start,end] = getShapeStringCoords()
    for i in range(start,end):
        for j in range(0,7):
            if grid[i][j] == "@":
                grid[i] = grid[i][:j] + "." +grid[i][j+1:]
                grid[i] = grid[i][:j-1] + "@"+grid[i][j:]

def moveDown():
    [start,end] = getShapeStringCoords() 
    for i in range(end,start-1,-1):
        for j in range(0,7):
            if grid[i][j] == "@":
                grid[i+1] = grid[i+1][:j] + "@" + grid[i+1][j+1:]
                grid[i] = grid[i][:j] + "." +grid[i][j+1:]

def rockToRest():
    [start,end] = getShapeStringCoords()
    for i in range(start,end):
        grid[i] = grid[i].replace("@","#")     

def removeUpperEmptySpace():
    while("#" not in grid[0]):
        grid.pop(0)
            


def fall(s, index):
    global currWind, input
    while True:
        wind= input[currWind]
        collision = checkLRCollision(wind)
        
        if not collision:
            if wind == ">":
                moveRight()
            if wind == "<":
                moveLeft()
        downMvnt = checkDownMvnt()
        if downMvnt:
            moveDown()
        else: 
            rockToRest()
            removeUpperEmptySpace()
            currWind = (currWind + 1) % len(input) 
            if currWind == 0:
                    if s[0] == ["@","@","@","@"]:
                        txt="index {}, new loop"
                        print(txt.format(rock))
            break
        currWind = (currWind + 1) % len(input) 
        if currWind == 0:
            if s[0] == ["@","@","@","@"]:
                txt="index {}, new loop"
                print(txt.format(rock))



def getLenght(times):
    rock = 0
    while rock < times:
        initializeGrid(shapes[rock%5])
        fall(shapes[rock%5], rock)
        rock = rock +1
    return len(grid)-1

### Part 2 ####
input = ">><<<<>><>><>><<>><<<<>><<<<>><<<>>><<>><>>><<<<>>>><<>><<<>>>><<>><<>>><>><<>>><<<<>><>>><<>><<>>><<<><>><<><<<<>><>>><<>>><<>><<<><<><<<>>>><<>>>><<<<><<<<>>><<<<>>><>><<<><>>><<<<>>>><<<>>><<<<>>>><>>>><<><<<<>>>><<<<>><<<<><<><<>>>><>>>><<<<>><>>><<<>>><<><<<>>>><<>><>>><>>><<><<>>>><<>><<>>>><<>>>><<<>>><<<>>><<<<>><<>>><>>>><>>>><<>>>><><<><<<<>>><<>><<<<>><<<<><<<<><<><<><>><<><<<><<<>>><<>>><<>><>>><<>>>><><<>><<<<><<<>>>><<<<>>>><<<<>>><<<>>><>>><<<<><<>>>><<>>><>><<<>>><<<>>><>>><><>><<<<>>><<<>>><>>>><<<<><><<<>>><<<>>><<<>>><<<>>>><<<>>><<<<><<<>>>><<<>><>>>><><>>><<<>><<<>>><>>><<<><<>><>>><<<<>><<<>>>><>><>>>><>>><<<<>>>><<>><<<><<>>><<>>>><<<<><<<>>>><>><<>><<<<>>><<><<<<><<<>><<<><>>><<>>>><<<<>><<>>>><<><>>>><<<>>><<<<><>><<>>>><>>><>><<<>><<<>>><<>>>><<<>>><>><><<<>><><<>>>><<<<>>>><<>>><<<<>>><<<>><>><><<>>><<<>>><<<><<>><<>>>><<<>><<>><<<<>>>><<<><<>>><>>><<<<>><><<<>><<<>><<><<>><<<>>>><<>>>><><<<>>>><<<><<><>>>><<<<>>>><>>><<<>>><>>>><<<<><><<><<<<><<<<>>><<><<<>>><<<><<<<>>>><<<>>><<<><>><>>>><>><<><<<<>>>><>><<<<>><<>>>><<>>>><<<<>>>><>>><<<<>>><<><<<>><<<<>>>><<<>><<<<>>>><<<<><<><>><<<>>><<<<>>><<<<>><<<>><<<>><<>><<<>><<<<>>><<<<>>><<>>><<<<>>>><<><<<>><>>><<<>>><<<>><<><>>><<><<>>>><<>>>><>>><>>><<<<><<>>><>>>><<<<><<<>>><>>>><>>><<<<>>>><>>>><><<>>><<<<>>><<>>><<<>>>><<<>>>><<<<>><><<>><<<>><<<>><<<<>>><<<<>><<<>>>><<>>><<<>>><>>>><<<<>>>><<>><>><<<<>>>><<<<>>>><<>>><<<>>><<<>>>><<>>>><<>><<>>>><<>>>><<<<><<<<>>>><<>><<>>><>>><<<><<<>>><<><<<<>>><<<>>><<>>>><<<><<<>>>><><<<>>><<<<><<>>>><<<>><>><<>>><>>><<<>>>><>>>><<<>><<>><<<<><<>><<<<>><<<<><><<<<>>><<<>>>><<<<>>><<<>>><<<>>>><>>><><>>><<>>><>>><<<><<<>><<>><<<<><<>>><<>>>><>>>><><<<<><<>><<<<>>><>><<>><<<<>><<<>>>><<<<>><<<>>><>>>><>><>><<<<>><>>>><>>>><<<>><<<>>>><<>><<>>><<<<><<<<><<>>>><<<<>><<<>>><<>>><><<<><<<>>>><>>>><>><>>><>>><<<<>>>><<<>>><>>>><<<<>>><<><<<><<>>><<><<<<>><>>><<><<<>>><<<<>><<><<<<>>>><<<><><<><>>><<<>><<<<><<><<<<>><><>>><>>>><<<<>><<<><<<>><<><<>><<<><<>>>><<>>>><<<<>>>><<<>>>><<>><>>><<>>><<<<><><<><<>>>><<<<><<<<><<<>>>><<<>>>><<>><<<>>>><<>>>><<><<>>>><>>>><<<>>><<<>><<><<>>><><><<<<>><<<>><<<>><>><<<>><<>>>><<<<>><>><<<<>>><<<<>>>><<<>>>><>><<<<>>><<<<><<<><<<<>><<<>>><<>>><<<<>><>>>><<>>>><<<>>><><>>><<<>>>><<<>>>><<<>>><>>><<<>>>><<<<>><<<<><<<<>>><<<<>><<>><>>><<<<><<><<<<>><><<>><<<<>>>><>>>><><<<<><>><<<<>>><>><<<<>><<<<>>><<><<<>><>>><<<>>><<<>>><<<>><>>>><<>>><<><<>><<<>>><<<<><<>><<<>><<><>><<>><>>>><>>><<<>>>><<<>>>><<<>><>><<<<>>><<><<>>><>>><<<<>>><<<><<<>>><>>>><<>>>><<>>><<<>><<<>><<<>>>><<>><<<<>><<>>>><<<<>>>><<>>>><<<<>>>><<>>><<<<>><<<<>><<<>>>><<<<>>><<<<><<<>>><>>>><<<<>><<<>>><<><<<>>><<<<>>>><<<<>><<>>><<<>><>>><<<>>>><<<><<<>>>><<><<<<>>>><>>>><<<<><<><<<<>><<<<><><>>><><<<<>>>><<<<><<>>>><<<<>>>><<<><<>>><<>>><><<<<>>><<>><<<>><<<<>>><<><<<>>><<>><<<><<<<>>>><>><<<>><>>><><<>>><<<<>><<><<>>><<>><<>>>><<><<>>><<<<>>><<>>><>><>>><<>><<<<>>><><<<>>>><<<<>>>><<<>>>><>>>><<><<<<><<><>><>><><<<<>>><<>><<<<><<<<>>>><><<<<><<>><<><<><<<>>><><<<>>><<<<>>>><><<>><<>>>><<><<>>>><<<<><<<><<>>><<>>>><<<>><<<>>>><>>><<>>>><<<<>>><><<<>><<<<>>><<<<>><<<>><<<<>><>>>><><>>>><<<>>>><<>>>><<><<>>><>>>><<>>>><<>><<><><<<<>><<<>><<<>><<<>>>><<<<>><<<<>><<<><<<><>>><><<>><<<>>><>>><<<>>><><>><<<<>>><>>><<>>>><>>>><>><<<<>>><<<><<<<><><<<>>><<>>><><<<><<<<>>>><>>>><<<<>>>><<<><<>><><<<<><>><>>><>>><<<<><><<<>>><<<<>><<<<>><<<><<<<>>><<>>><<>>>><<<>><<<<><<<<>>><>><<><<<<>>>><<<>>><<>>><<<<>><<<>>><>>><<<<>>><<<<>>><<<>>>><>><<<>>>><<><<><<<<>><<><<<><<<<>><<>>><>>>><<><>><<<>><<<<>><<>><>>>><<<<>>>><<>>>><<>>><<><<<><<<><<<<>><<<<>><<>>>><>>><>><<<>>><<<>>>><<<<>>><<<>>><<<<>>>><<<>>><>><<<<>>>><<<>>>><<<<>>>><<>>><<><<>>><<<>>><>><<<<>><<>>><<<>>><<>>><<>><>>>><<<><<<<><<>>>><<><<<<><<<><<<>><<<><><<<>>>><>><<><<<<>>><>>><<<<><<>><<<<><<<<>><<>>><<>>><>>>><<>><<<<>><>>>><>>><>>><<>>><<<<>><><<<>>>><<<<><<<<>>>><<<>><<><>>><<>>>><<<<>>>><<>><<>>><><<<<>><<<>>><<<>><<>><>><<<<>><<>><>>><<<>><><<<>>>><<<<>><<>><<<>><<<>>>><>><<<><<<<>>><<<>>><<<>>><<>><<<<>><>>><<>>>><<<><<<<><<>>><>>><>><<<<>><<><<<<><<<<>>>><<<>>>><<<>>>><<<><<>>><<>>><<<>>><>>><<<<>>><<<<>>>><<><<<<>><>>><>>><<<>>><<<<>>>><>>>><<<>>>><<><><<>><<<><<<>>>><<<><<<>>><>><<<<>><<<<>>><<<>>>><<<>><<<><<<<>>><<<<>>>><<>>><>>>><<<><<<<><<<>>><<>><<<>>><>>>><<<<>>>><<<<><<<>>>><<><>>>><<>>><<>>>><<><<<<><<<<>><<<<>>><<<<>><>><<<>>>><<>><>><>><<>>><<<>><<<><>>><<<<>>>><<<>>>><<<>>>><<>>>><>>><<<>>><<<<>><<<>>>><<>><<>>>><>><<<<><<>>>><<<<>><<<<>><<<>>>><>>><<>><><<>>><<><<>><><<<<>>>><<<<>>>><<>>>><<<>><<<<><>>>><<>><<<<>>><<>>><<<>><<<>>><<<<><<<>>>><>><><>>>><<<>>><<<<><<<<>>>><<<>>>><<<<>><<><<<<>>>><>><<<>>><<<>>>><>>><<<<>>><<<<>><<<<>><<<<><<<<>>><<>>>><<<<>>><>>><<>>>><>><<>>><<>>><<<<>>>><<<<>><<<><>>><<<>><<><>><<<><<<<>>>><<<>><><<<<><<<<><>>>><>>><<>><>>><><<<<>>><><<<><<><<<>>><><<<>>>><<><<><<<>>><<<><>><>>><<<><<<<>>>><<<>><<<><<<<>><<<<><<<<>>><<<>>>><<<<>>><><<<>><<<<>>><>>>><<<>>><<>>><<<>>><<<<>>><<<<><<<>>><<<<><<<<>>>><<>>><<<<>>><<>><><>><<><>><<<>>><<>><>>><>><<<><>>><><>>>><<<><<<>>><<>>><><<<<>>>><<<><<<>>>><<<<>><<>>>><<<<>>><<<<>>>><<>><<<>>><<<><<>>>><<<>><<<<><<>><<<<>>><<>>><<><>>><<>>>><<<<><<>><<<<>>><<<<>>><<<>><<<>><<><<<<><<<<>>>><><<<>><<>>>><<<><<<<>><<>>>><>>><<>>><<>><<>>>><<<<><<><<<<><<<<>>>><<<<><<>>><<<><<<<>>><>>><<<>><<<<>>><<<<>>>><>>>><>>><<<>>><<<<>>>><>><<<<>><<<<>><<<>>>><>>><<<<>>><<>><<<<><>>>><>>>><<>><<<<>><><<<<>><>><<<>>><<<>>>><<<><><<>>>><<><<<>>><<>>>><<<><<<<>><>>><>><<><>><<>>>><<<><<<<>><><>>><>>><<>>>><<>>>><<<<><<>>>><<<>>><<>><<<<><<>>>><<><><><<><<<<>><<<>>><<><<<>><<<><<<>>>><><<>>><<<<><<><>>>><<<<>>>><<<><<>>><<<>>><<<>>>><<<>>><>><<>>>><<<>>><<<><>><>>>><<<<>><<>><<>><<<>><<>>>><>>>><>><><<>><>>>><><>>>><>><<>><<><<<>>><<<>>>><>>><<<><<<>>><>>><<<<>>><<>>>><<<>>><<<<>>><<<><<<<>>>><<>>><<<<><<<>>>><<><<<<>>><<>>><<<>><>>><<<<><<>>>><>><>><<<>>>><>>><<<>><<><<><<><<<>><<<><>><<<>><<<><>><>>>><<>><>>><<<<>>>><<><>>><<<>>>><<<><><<>>>><<<>>><><<<<>>>><<>>>><>>>><>>><<<>>>><<>>><<>>>><<<<>>>><<<>><<<<>>><><><>>>><<<<>>>><<<>>><<>>>><<>><<>>><>>>><<<<>>><><<><<<>>>><<><<<<>>><<>>><<<<>><<<><<>>><<<<>><<>>><><<>>>><<<>><<<>>><<<<>>><<<>><<<<><<>><<<<><<><<<><<<>>>><>><<<<>>>><>><<<>>><<>>>><<>>>><<><>>>><<<<>><<<><<>><<<<>>><<<>>>><<><>>>><><<<<><<<<>>>><<<<><<<<>>><<<<><<><<<<>><<<><<<<><<>>>><<><<>>><<><<<>>><>>>><<><<<>>>><<<>>>><<<>>><<>><<<><<<<><<><<<>>>><>><<>>><><<<>>>><<<>>>><<<<>><<>>><<<>>><<<>>>><>>><>>><<>>>><<<><>><>>>><<<><<<><<<><<>><<<<>>>><<<<>>>><<<><<<>>>><<<>>>><>>>><><>>>><>><<>><<<<>>>><<>>><<<>><<<>>>><<<>><<>><<<>><<<>><<>>><><<>><<<>><<<<>><<<<>><<<<>>><>>><<<<><>><><>>><>>>><<<>>>><<>>>><<<<>><<<>><<>>><>>>><<<<>>><<<>>>><<>>>><<>><>>>><<<<>>><<>>>><>><<>>><<<<>>>><>>>><<>><<><<<>>><>><><<<<>>>><<<<><>>>><<>>><<<<>><<<><<>>><<<<><<<<>>>><<<<><<>>>><>>><<>><<><>><<<<><>><<<<>><<<<><<<><<><<>>><<<<>><>>><><><<<<><<<>>><>>><>>><>><<<<>>>><<<<><>>><<>><<>>><>>>><<<>>><<>><>><<<<>>>><<<>><>><<<<>>>><<<><<<>>><><<<<>>><>>>><<>><<<>>>><<<<><<<<>>><<<<>>>><<<<>>><<<>><><<<>><<>>>><<><><<<<>>><<>><<<>>><<<<>><<<<>>>><<<<>>><<<>>>><>>>><><<>>>><<<>><<<<>><<<>>><<<><>>><<<>>>><<>><<<>><<<<><>>><<<<>>>><>>>><<><>><<<<><<<>>><>>><<>><>><><<<<><<<<>>><<>>><><<<<>>>><<<>>>><>>><<>>><<<<>>><<>>>><<>>><<>>><<<>>>><<>>><<<><>>><<<>>>><<><<<<><<<<>>><<<>>>><<<<>>><<>><<>><<><<<><<<<>><<<>><><<>><<<<>>>><<<>><<<>>>><<<<>><>>><<<<><<<>><<>>>><<>>><>><<<>>><>>>><<<<>>><<<<>>><<>>><<>><<>>>><<<<>><>><>>><>>><<<>>><>><<<<>>><>>>><<>><<<<>>>><<<<>>><<<<>>><<<<>>>><><<>><<>>>><<<<><<>>>><<<>>><<<<>><<<<><<><<>><<<<>>>><<<>>><<<>>><>>><<<<>>><<><<<><<><<<><<>>>><><<>>><<<<>><<<>><<<<>>>><<<>>><>><>>><<<>>><<>><><<>>><<<<>>>><<<>>>><<<>>><<>>>><<<<><<><<>>>><><<<<>>>><>>>><<<>>><<<<>><<>>>><<<<>><<>><<>><><>>><<<><<<>>><><<<<><<>>>><<>><<><<<<>>><<<>><<>>>><<>>>><>>><<<><<<<>>>><<>><>><<<><<<>>><>><>><>><><<>>><>><>><<>>>><<>>>><<<<>>>><<<><>><>>><<<>><<<><>>><<<>>><<><<<><<<><<>>><<<<>><<<>>>><<>>><>>>><<>>><<<<>>>><<>>>><<>>>><<>>><<<>>>><<><><>><<<>>>><<<>>>><<<<>>><<<>><<<><<><<<<>>><<<<>><<<>>><>>><><<>>><>>><<<<>><<<<>><<<>><<<><<>><<<<><<>>><>>>><><<<<><>>><<>>>><<<>>>><<>><>><>>><<>><<<<>>>><<<<>><<<<>><<<>><<<>>><<>>><<><>>>><<><<<>>>><<>>><<<<><<<>><<><<<<>>><<>>>><<<<>><<<<>>>><<<<>><<>>><<<><<>><<<<>>><>>><<><<>>>><>><<<>>>><<>>><<><>>>><<>>><<<<>><<>><<<><<>>>><<<>>>><<<<>><<<<><<<<><<<>>><>>><>>><<<<>><><<<<>>>><<<>><<><<><<<>>><>><<<<>>><<><<<>>>><<>>>><<<<>>><><<<<><><<<<><<<>>>><<>><<<<>>><<<><<<<>><<<<>>>><<<>>>><<<>>><<>>><<<>><<>>><<>><<><><<<>><>>><<<<>>><<<<>>><<><><<><<>>><>><><><<<><<>><<>>><<<<>>><<<>>><><<<>>>><<<<>>>><<>><><<<><<<<>>>><>>><<<>>><<<><><<<<>>>><<>>><><<<<>><<<<>>><><<<<>>><<>><<<<>><<>>><<<<>>>><<<<>>>><><<>>><<><<<<><<<<>><<<<>>><><>><<<<><<><<>>><<<<>>>><<<<>><<<<><>><<<<>>><><<<>><>><<<<>>><<<<>><<>>>><<<>>>><<<>><>>>><>><<<<><>><<<<>>>><<<<>>>><<>>>><<<<>><>>><>>><>><<<>>><<><<<>>><><<<<>>>><><>>>><<<>><<<>><<>><>><>>><<<<><<<<>>>><>>>><<>><<<>>>><<<<>>><<<>>>><<><><<<>><<<<>>>><>><<>>>><<<>>>><<<><<>><<<><<<<>>><<<<>><>>><>>>><<>>><<<<>>><<<>>>><<<>>>><<<>>>><<><>>>><<>>>><><<<>>>><<<>>><>>>><>>><<><<>>><<>>><<><<<<>>><<<<>>>><<<<>>>><>>><<<>>><>>>><<><<<<>>><<<<>>>><<><<<<>><<><<<>>>><><>>>><<>>><<>>><>><<<<>><<<<><>>>><<<>>>><<<>><<<<>>><<<<>><<<<>>><>><<>><>>><<>>>><<><><<<>>><<<>><<<<>>><<><<<<>><<<>>>><<>>>><>><>>>><<>>><><>>>><>>>><<<>><<>><>><>><<<<><<<>>><<<>>>><<>><<><<<<>>><>><>>><>><><<<>><<<>>><<<>>>><<<<><<<>>><><>><<<>>><<<>>>><>>><<><<<<>><><<<><<<>>><<<<><<>>><>>>><<<<>>>><<<<><>><<><>>>><<>>><>>>><<<><>>><<<><<<<>><<<>><><<<>><><<>>><<>>>><>>><<>>>><<<<>><>>><>><<<>>><><<>>><<<<>><>>>><<<>><<<><><<><<<>>><>><<<>><<<<>><<>>><<<<><<>>><<<>><>><<<>>><<>>>><<<><<<>><<>>><<>><>>>><>><<<<><<<><<<<>><<>>>><<>><<<>>>><<>>><<<<>><>>><>><<<>>><<<>><<<<>>><>>><>>><<<<>>><<>>><<<>><<><<<>>><>>><<>>><<<<>><<>><><<<<><><<<<>>>><<<<><<<<><<<>>>><<<<>><<><<<>><<><>><<<<>>><<<>>>><<<<>><<>>><<<><<<<><>>><<<>>><<<<>><<<<>><<<<>>><<<<>>><<><<<<>>><<<><<>>>><<<>>><<<>><<<>><><<<>>><<>>><>>>><<<<><>>>><>>><<<<>>><>>><>><<<>>"
input = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
totalLen = 0
grid=["#######"]
currWind = 0
times =  1000000000000
count = 0
lcf = 5 * len(input)
rock = 0
while rock < 10000:

    initializeGrid(shapes[rock%5])
    fall(shapes[rock%5],rock)
    rock = rock +1
print(len(grid))
print("Hello")
# while(divider > 0):
#     grid=["#######"]
#     count = getLenght(60000)
#     txt = "{} time, len is: {}"
#     print(txt.format(divider, count))
#     divider = divider +1

print("Part1: ", getLenght(2022))



### Part 1 ####
# rock = 0
# grid = []
# grid = ["#######"]
# currWind=0
# while rock <=2021:

#     initializeGrid(shapes[rock%5])
#     fall(shapes[rock%5])
#     rock = rock +1

# print("Part1: ", len(grid)-1)
