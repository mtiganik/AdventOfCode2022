f = open("day20/day20.txt")
vals = []
lst = []
cnt = 0
for x in f:
    vals.append((cnt,int(x.strip())))
    lst.append((cnt,int(x.strip())))
    cnt = cnt+1

size = len(vals)

def mix(vals, lst):
    for n in vals:
        oi = lst.index(n)
        ni = (oi + n[1]) % (len(lst) - 1)
        del lst[oi]
        lst.insert(ni if ni else len(lst), n)

mix(vals,lst)
zp = [
    idx for idx, tup in enumerate(lst) if tup[1] == 0
][0]

el1, el2,el3 = lst[(zp+1000)%size][1], lst[(zp+2000)%size][1], lst[(zp+3000)%size][1]
print(el1,el2,el3)

print("Part1:", el1+el2+el3)
