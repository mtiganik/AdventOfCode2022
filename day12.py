f = open("day12.txt")

grid = []
for x in f:
    x = x.strip()
    x = list(x)
    grid.append(x)

path = [['.']*len(grid[0]) for _ in range(len(grid))]

X,Y,destX,destY=0,0,0,0
for x in grid:
    if "S" in x:
        X = x.index("S")
        Y = grid.index(x)
    if "E" in x:
        destX = x.index("E")
        destY = grid.index(x)
    print(x)
currChar = 'a'
while X != destX or Y != destY:
    #check down
    if Y != len(grid)-1:
        if path[Y+1][X] == '.':
            if ord(grid[Y+1][X]) == ord(currChar) +1:
                path[Y][X] = "v"
                Y = Y+1
                currChar = grid[Y][X]  
                continue
            elif ord(grid[Y+1][X]) == ord(currChar):
                path[Y][X] = "v"
                Y = Y+1
    #check right
    if X != len(grid[0]) -1:
        if path[Y][X+1] == '.':
            if ord(grid[Y][X+1]) == ord(currChar) +1:
                path[Y][X] = ">"
                X = X + 1
                currChar = grid[Y][X] 
                continue
            elif ord(grid[Y][X+1]) == ord(currChar):
                path[Y][X] = ">"
                X = X + 1
    #check top
    if Y != 0:
        if path[Y-1][X] == '.':
            if ord(grid[Y-1][X]) == ord(currChar) +1:
                path[Y][X] = "^"
                Y = Y - 1
                currChar = grid[Y][X]
                continue
            elif ord(grid[Y-1][X]) == ord(currChar):
                path[Y][X] = "^"
                Y = Y - 1
    #Check left
    if X != 0:
        if path[Y][X-1] == '.':
            if ord(grid[Y][X-1]) == ord(currChar) +1:
                path[Y][X] = "<"
                X = X - 1
                currChar = grid[Y][X]
                continue
            elif ord(grid[Y][X-1]) == ord(currChar):
                path[Y][X] = "<"
                X = X - 1


for x in path:
    print(x)
print(X,Y,destX,destY)