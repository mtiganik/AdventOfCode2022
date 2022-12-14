f = open("day8.txt")
grid = []
for x in f:
    grid.append(list(map(int,x.strip())))

countGrid = [[0]*len(grid[0]) for _ in range(len(grid))]

def getViewCnt(i,j):
    #Top
    topCnt = 0
    for k in range(i-1,-1,-1):
        if grid[k][j] >= grid[i][j]:
            topCnt = topCnt+1
            break
        else: topCnt = topCnt+1
    #Bottom
    bottomCnt = 0
    for k in range(i+1,len(grid)):
        if grid[k][j] >= grid[i][j]: 
            bottomCnt = bottomCnt+1
            break
        else: bottomCnt = bottomCnt +1

    #Left
    leftCnt = 0
    for k in range(j-1,-1,-1):
        if grid[i][k] >= grid[i][j]: 
            leftCnt = leftCnt+1
            break
        else: leftCnt = leftCnt +1
    
    #Right
    rightCnt = 0
    for k in range(j+1,len(grid[0])):
        if grid[i][k] >= grid[i][j]:
            rightCnt = rightCnt+1
            break
        else: rightCnt = rightCnt+1
    
    return topCnt * bottomCnt * leftCnt * rightCnt


for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        countGrid[i][j] = getViewCnt(i,j)


maxScore = 0
ii, jj = 0,0
for i in range(0,len(grid[0])):
    for j in range(0,len(grid)):
        if countGrid[i][j] > maxScore:
            maxScore = countGrid[i][j]
            ii = i
            jj = j
txt = "Max score {} at [{}][{}] "
print(txt.format( maxScore, ii, jj))

