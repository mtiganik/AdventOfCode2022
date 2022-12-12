f = open("day12.txt")

grid = []
for x in f:
    x = x.strip()
    x = list(x)
    grid.append(x)

def containsAll(str, set):
    """ Check whether sequence str contains ALL of the items in set. """
    return 0 not in [c in str for c in set]

def upDownEnd(str):
    if "v" in str:
        if "^" in str: 
            return True
    if "<" in str:
        if ">" in str: 
            return True
    return False

def shouldGo(str, strlst, p,p1):
    for x in strlst:
        if x == str + p:
            return False
        if x == str + p1:
            return False

    return True

# if[ele for ele in strlst if(ele[:-1] in str1)]:
#     print("str is in list, ", str1)
#path = [['.']*len(grid[0]) for _ in range(len(grid))]
sX,sY,destX,destY=0,0,0,0
for x in grid:
    if "S" in x:
        sX = x.index("S")
        sY = grid.index(x)
    if "E" in x:
        destX = x.index("E")
        destY = grid.index(x)

currChar = 'd'
move = 0
atmt = 0
wasMovement = True
path = ""
paths = [""]
validPaths = [""]
X,Y = sX,sY
for i in range(0,20):
    atmt = i
    while (X,Y) != (destX,destY):
        wasMovement = False
        #check down
        if Y != len(grid)-1:
            if shouldGo(path,paths,"vX","vD"):
                if ord(grid[Y+1][X]) == ord(currChar) +1 or (grid[Y+1][X] == 'E' and currChar=='z'):
                    path = path + "v"
                    Y = Y+1
                    currChar = grid[Y][X]  
                    wasMovement = True
                    continue
                elif ord(grid[Y+1][X]) == ord(currChar):
                    path = path + "v"
                    Y = Y+1
                    wasMovement = True
                    continue
        #check right
        if X != len(grid[0]) -1:
            if shouldGo(path,paths,">X",">D"):
                if ord(grid[Y][X+1]) == ord(currChar) +1 or (grid[Y][X+1] == 'E' and currChar=='z'):
                    path = path + ">"
                    X = X + 1
                    currChar = grid[Y][X] 
                    wasMovement = True
                    continue
                elif ord(grid[Y][X+1]) == ord(currChar):
                    path = path + ">"
                    wasMovement = True
                    X = X + 1
        #check top
        if Y != 0:
            if shouldGo(path,paths,"^X","^D"):
                if ord(grid[Y-1][X]) == ord(currChar) +1 or (grid[Y-1][X] == 'E' and currChar=='z'):
                    path = path + "^"
                    Y = Y - 1
                    currChar = grid[Y][X]
                    wasMovement = True
                    continue
                elif ord(grid[Y-1][X]) == ord(currChar):
                    path = path + "^"
                    wasMovement = True
                    Y = Y - 1
        #Check left
        if X != 0:
            if shouldGo(path,paths,"<X", "<D"):
                if ord(grid[Y][X-1]) == ord(currChar) +1 or (grid[Y][X-1] == 'E' and currChar=='z'):
                    path = path + "<"
                    X = X - 1
                    currChar = grid[Y][X]
                    wasMovement = True
                    continue
                elif ord(grid[Y][X-1]) == ord(currChar):
                    path = path + "<"
                    X = X - 1
                    wasMovement = True

        #Check dead end    

        if containsAll(path[-4:], "^<v>") or upDownEnd(path[-2:]) or wasMovement == False:
            #print("Dead end reached on path: ", path)
            if containsAll(path[-4:], "^<v>"): path = path[:-4]
            if path == "": 
                break
            path = path + "X"
            paths.append(path) 
            # atmt = atmt +1
            path= ""
            X,Y,currChar = sX,sY,'d'
    else:
        print("reach destination!!")
        path = path + "D"
        paths.append(path) 
        validPaths.append(path)
        path= ""
        X,Y,currChar = sX,sY,'d'
        #print(path)
def lenVal(e):
    return len(e)
validPaths.sort(key=lenVal)
for x in validPaths:
    print(x, len(x)-1)
print(path)
print(X,Y,destX,destY)