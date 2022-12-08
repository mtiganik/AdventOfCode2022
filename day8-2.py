f = open("day8.txt")
grid = []
for x in f:
    grid.append(list(x.strip()))

countGrid = []
zeroList = [0]*len(grid[0])
for i in range(0, len(grid)):
    countGrid.append(zeroList)

def getViewCnt(i,j):
    cnt = 0
    #Top
    topCnt = 0
    if i > 0:
        for k in range(i-1,0,-1):
            if grid[k][j] > grid[i][j]:
                break
            else: topCnt = topCnt+1
    #Bottom
    bottomCnt = 0
    if i < len(grid) -1:
        for k in range(i+1,len(grid)):
            if grid[k][j] > grid[i][j]: break
            else: bottomCnt = bottomCnt +1
    else:
        txt = "{}{} is skipped from bottom"
        print(txt,format(i,j))

    #Left
    leftCnt = 0
    if j > 0:
        for k in range(j,0,-1):
            if grid[i][k] > grid[i][j]:
                break
            else: leftCnt = leftCnt +1
    
    #Right
    rightCnt = 0
    if j < len(grid[0]) -1:
        for k in range(j+1,len(grid[0])):
            if grid[i][k] > grid[i][j]:
                break
            else: rightCnt = rightCnt+1
    
    return topCnt * bottomCnt * leftCnt * rightCnt


for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        countGrid[i][j] = getViewCnt(i,j)
for x in countGrid:
    print(x)

for x in grid:
    print(x)