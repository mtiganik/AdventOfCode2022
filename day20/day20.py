f = open("day20/day20.txt")
data = []
sort = []
for x in f:
    data.append(int(x.strip()))
    sort.append(int(x.strip()))


size = len(data)
for i,x in enumerate(data):
    ii = sort.index(x)
    val = sort[ii]
    if val != 0:
        delimin = int(abs(val)/val)
        bwc = 0
        for j in range(0,val, delimin):
            ci, ni = abs((size+ii+j+bwc))%size, abs((size+ii+j+delimin+bwc))%size
            if ci == 1 and ni == 0 and delimin==-1:
                sort.pop(1)
                sort.append(val)
                bwc = bwc -1
            else: sort[ci], sort[ni] = sort[ni], sort[ci]
    

for x in sort:
    print(x)