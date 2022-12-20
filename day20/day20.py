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
        for j in range(0,val, delimin):
            ci = sort.index(val) 
            ni = (ci + delimin)%size 
            if ci == 1 and ni == 0 and delimin==-1:
                sort.pop(1)
                sort.append(val)
            elif ci == size -2 and ni == size -1 and delimin == 1:
                sort.remove(val)
                sort.insert(0,val)
            else: sort[ci], sort[ni] = sort[ni], sort[ci]
    
zp = sort.index(0)
el1,el2,el3 = sort[(zp+1000)%size], sort[(zp+2000)%size], sort[(zp+3000)%size]
print(el1,el2,el3)

print("Part1:", el1+el2+el3)