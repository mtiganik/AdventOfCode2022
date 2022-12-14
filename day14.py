
rangey = 168 # if excpection put it bigger
# rangey = 12 #test
grid = [["."]*1000 for _ in range(rangey)]

f = open("day14.txt")
sand = []
for x in f:
    points = x.rstrip().split("->")
    p2ds=[]
    for y in points:
        p = y.split(",")
        p = [eval(i) for i in p]
        p2ds.append(p)
    sand.append(p2ds)
grid[0][500] = "+"
for x in sand:
    for k in range(0, len(x)-1):
        point = x[k]
        stepx = 1 if x[k][0] < x[k+1][0] else -1
        stepy = 1 if x[k][1] < x[k+1][1] else -1
        for i in range(x[k][0],x[k+1][0] + stepx, stepx):
            grid[point[1]][i] = "#"
        for j in range(x[k][1], x[k+1][1] + stepy, stepy):
            grid[j][point[0]] = "#"



def findSpotToFall(y,x):
    stp = 1
    while(y < len(grid)-1):
        if(grid[y+1][x]) == ".":
            y = y+1
        else:
            if grid[y+1][x-1]==".":
                findSpotToFall(y+1,x-1)
            elif grid[y+1][x+1] == ".":
                findSpotToFall(y+1,x+1)
            else:
                grid[y][x] = "o"
            break



#find grid length:
floor = 0
for i in range(0,len(grid)):
    if "#" in grid[i]:
        floor = i
floor = floor  + 2
fl = ["#"]*1000
grid[floor] = fl 

checker = 1
cycle = 0
for i in range(0,100000):
    cycle = cycle +1
    findSpotToFall(0,500)


for x in grid:
    str = "".join(x[420:560:1]) #test
    # str = "".join(x[490:510:1]) #test
    print(str)

cnt = 0
for x in grid:
    cnt = cnt + x.count("o")

print(cnt)

#Part1

# checker = 1
# cycle = 0
# for i in range(0,1000):
#     cycle = cycle +1
#     findSpotToFall(0,500)

# for x in grid:
#     str = "".join(x[420:560:1]) #test
#     # str = "".join(x[490:510:1]) #test
#     print(str)
# cnt = 0
# for x in grid:
#     cnt = cnt + x.count("o")

# print(cnt)