def checkTop(i,j):
    for k in range(0,i):
        if grid[k][j] >= grid[i][j]:
            return False
    return True

def checkBottom(i,j):
    for k in range(i+1, len(grid)):
        if grid[k][j] >= grid[i][j]:
            return False
    return True

def checkLeft(i,j):
    for k in range(0,j):
        if grid[i][k] >= grid[i][j]:
            return False
    return True

def checkRight(i,j):
    for k in range(j+1, len(grid[0])):
        if grid[i][k] >= grid[i][j]:
            return False
    return True

f = open("day8.txt")
grid = []
for x in f:
    grid.append(list(x.strip()))

count = 0

#edge trees:
count = 2*len(grid[0]) + 2*len(grid) - 4
print(count)

for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        if checkTop(i,j) or checkLeft(i,j) or checkBottom(i,j) or checkRight(i,j):
            count = count +1

print(count)
