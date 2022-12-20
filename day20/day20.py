f = open("day20/day20.txt")
vals = []
lst = []
for x in f:
    vals.append(int(x.strip()))
    lst.append(int(x.strip()))


size = len(vals)
for i,x in enumerate(vals):
    ii = lst.index(x)
    val = lst[ii]
    lst.pop(ii)
    if(ii+val==0):
        lst.append(val)
    elif(ii+val == size-1):
        lst.insert(0,val)
    elif val > size and val%size > ii:
        lst.insert((ii+val+1)%size, val) #debug it
    elif ii+val >= size: 
        lst.insert((ii+val+1)%size, val)
    elif val < 0 and -val >= size: 
        lst.insert((ii+val-1)%size,val)
    else :
        lst.insert(ii+val, val)
    
zp = lst.index(0)
el1,el2,el3 = lst[(zp+1000)%size], lst[(zp+2000)%size], lst[(zp+3000)%size]
print(el1,el2,el3)

print("Part1:", el1+el2+el3)