data = []
f = open("day18/day18.txt")
data = []
for k in f:
    k = k.rstrip().split(",")
    x,y,z = int(k[0]), int(k[1]), int(k[2])
    item = [x,y,z]
    data.append(item)

sum = len(data)*6

def checkCollision(i,j):
    if abs(i[0]-j[0]) + abs(i[1]-j[1]) + abs(i[2]-j[2]) == 1:
        return True
    return False

# for i in range(0,len(data)-1):
#     for j in range(i,len(data)):
#         if checkCollision(data[i],data[j]):
#             sum = sum -2
sum = 4418
# print("Part 1:", sum)


for i in range(1,20):
    for j in range(1,20):
        for k in range(1,20):
            if [i,j,k] in data: continue
            elif [i-1,j,k] in data and [i+1,j,k] in data and [i,j-1,k] in data and [i,j+1,k] in data and [i,j,k-1] in data and [i,j,k+1] in data:
                sum = sum-6

print(sum)
