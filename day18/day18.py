data = []
f = open("day18/day18.txt")
data = []
for k in f:
    k = k.rstrip().split(",")
    x,y,z = int(k[0]), int(k[1]), int(k[2])
    sArea = 6
    #item = {"x":x,"y":y,"z":z,"A":6}
    item = [x,y,z]
    data.append(item)

sum = len(data)*6

def checkCollision(i,j):
    if abs(i[0]-j[0]) + abs(i[1]-j[1]) + abs(i[2]-j[2]) == 1:
        return True
    return False

for i in range(0,len(data)-1):
    for j in range(i,len(data)):
        if checkCollision(data[i],data[j]):
            sum = sum -2

print(sum)