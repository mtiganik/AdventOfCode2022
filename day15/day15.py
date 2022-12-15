f = open("day15/day15.txt")

y = 2000000
biy = []
vals =[]
xmax,ymax,xmin,ymin = 0,0,0,0
for x in f:
    txt = x.split()
    sx= int(txt[2].split("=")[1].rstrip(","))
    sy = int(txt[3].split("=")[1].rstrip(":"))
    bx = int(txt[8].split("=")[1].rstrip(","))
    by = int(txt[9].split("=")[1].rstrip())
    if sx > xmax or bx > xmax: xmax = max(sx,bx)
    if sx < xmin or bx < xmin: xmin = min(sx,bx)
    if sy > ymax or by > ymax: ymax = max(sy,by)
    if sy < ymin or by < ymin: ymin = min(sy,by)
    if by == y: biy.append(by)
    if sy == y: biy.append(sy)
    dist = abs(sx-bx)+abs(sy-by)
    val = {"sx":sx, "sy":sy,"bx":bx,"by":by,"d":dist}
    vals.append(val)

biy = list(dict.fromkeys(biy))
# print(biy)

cnt = 0
for k in range(xmin-10000,xmax+160000):
    didReach = False
    for idx, x in enumerate(vals):
        if(abs(x["sx"]-k)+abs(x["sy"]-y) <= x["d"]):
            # print("abs x:", abs(x["sx"]-k))
            # print("abs y:",abs(x["sy"]-y))
            # print("signal reached to x=:",k)
            cnt = cnt +1
            break
cnt = cnt - len(biy)
# print(xmin,xmax)
# didnotReac = abs(xmax-xmin) - cnt
# print(didnotReac)
print(cnt)
# for x in vals:
#     print(x)
####B######################