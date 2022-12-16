import time
start_time = time.time()


f = open("day16/day16.txt")
maxDist = 1000
points = []
nodes = []
for x in f:
    x = x.rstrip().replace(";","").replace(",","").split()
    point = x[1]
    rate = int(x[4].split("=")[1])
    lt=  x[9:]
    for n in lt:
        #if not any([n, point] in sublist for sublist in nodes):
        if [n,point] not in nodes:
            node = [point, n]
            nodes.append(node)
    tg = {"p":point, "r":rate,"visited": False, "dist":maxDist}
    points.append(tg)


def getCurrentPoint():
    minVal = maxDist
    pointToreturn = 0
    for x in points:
        if x["dist"] < minVal and x["visited"] == False:
            minVal = x["dist"]
            pointToReturn = x
    return pointToReturn

def getNodes(point):
    returnNodes = []
    for x in nodes:
        if point["p"] in x:
            returnNodes.append(x)
    return returnNodes

def setDistanceToNearbyNodes(pf, pn):
    for node in pn:
        ptn = node[1] if node[0] == pf['p'] else node[0]
        pt = [d for d in points if d['p']==ptn][0] 
        dst = pf['dist'] + 1
        pt['dist'] = dst if dst <  pt['dist'] else pt['dist'] 

def setStartPoint(name):
    for x in points:
        x["dist"],x["visited"]=maxDist,False
    startPoint = [d for d in points if d["p"] == name][0]
    startPoint["dist"] = 0

numOfMaxVals = 5
start = "AA"


#See asi tagastab 5 kõige suurema flowiga kanalit 
mins = 30
#def getMaxValsForCurrentPoints(currentPoint, numOfMaxVals)
startpoint = setStartPoint(start)

cnt = len(points)
while(cnt > 0):
    point = getCurrentPoint()
    pointNodes= getNodes(point)
    setDistanceToNearbyNodes(point,pointNodes)
    point["visited"] = True
    cnt = cnt-1

for x in points:
    x["flow"] = (mins-(x["dist"]+1))*x['r']

newNodes = sorted(points, key = lambda d: d['flow'], reverse=True)[0:numOfMaxVals]


for x in newNodes:
    print(x)

print("Process finished --- %s seconds ---" % (time.time() - start_time))
