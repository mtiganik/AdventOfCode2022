grid =[
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
    [1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

ey, ex = 19,19
xMax, yMax= len(grid), len(grid[0])
visited = [[False]*xMax for _ in range(yMax)]
dist = [[1000]*xMax for _ in range(yMax)]

xc,yc = 0,0
dist[yc][xc] = 0
visited[yc][xc] = True
def findSetNearbys(y,x):
    currDist = dist[y][x]
    nbys = []
    nby = []
    if x > 0: nby.append(list((y,x-1)))
    if y > 0: nby.append(list((y-1,x)))
    if x < len(grid[0])-1: nby.append(list((y,x+1)))
    if y < len(grid)-1: nby.append(list((y+1,x)))
    for k in nby:
        if grid[k[0]][k[1]] == 0 and visited[k[0]][k[1]] == False:
            dist[k[0]][k[1]] = currDist + 1
            nbys.append(k)
    return nbys

def getUnvisitedMinDist():
    minDist = 2000
    #Loop only to find min dist
    for i in range(0, len(grid)):
        for j in range(0,len(grid[0])):
            if visited[i][j] == True:
                continue
            else:
                if dist[i][j] <= minDist:
                    minDist = dist[i][j]
    return minDist

def getNextPoint():
    mindDist = getUnvisitedMinDist() 

    pwmindist = []
    for i in range(0, len(grid)):
        for j in range(0,len(grid[0])):
            if visited[i][j] == True:
                continue
            elif dist[i][j] == mindDist:
                pwmindist.append(list((i,j)))
    return pwmindist

            


while visited[ey][ex] == False:
    findSetNearbys(yc,xc)
    visited[yc][xc] = True
    npts = getNextPoint()
    if len(npts) == 0:
        break
    [yc,xc] =npts[0]

print("Done")