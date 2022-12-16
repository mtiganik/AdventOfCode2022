f = open("dijkstra.txt")

dMax = 1000
node = {"f":"0", "to":"1","d":4}
nodes = []
points = ["0"]
pl = []
start = "0"
end = "5"
#0 to 1 is 4
        
for x in f:
    x = x.rstrip().split()
    f = x[0]
    t = x[2]
    d = int(x[4])
    vals = {"f":f,"t":t,"d":d}
    nodes.append(vals)

for x in nodes:
    if x["f"] not in points: points.append(x["f"])
    if x["t"] not in points: points.append(x["t"])

for x in points:
    p = x
    if p != start:
        pl.append({"p":p,"v":False,"d":dMax})
    else:
        pl.append( {"p":start,"v":False,"d":0})

def getCurrPoint():
    minVal = dMax
    point = ""
    for x in pl:
        if x["d"] < minVal and x["v"] == False:
            minVal = x["d"]
            point = x
    return point

def getNodes(point):
    f = point["p"]
    pointNodes = []
    for x in nodes:
        if x["f"] == f or x["t"]==f:
            np = x["f"] if x["f"] != f else x["t"]
            #Kontrollime et seda punkti ei ole me jälginud
            for p in pl:
                if p["p"]== np and p["v"]==False:
                    #pointNodes.append(x)
                    pointNodes.append({'f':f,'t':np,'d':x['d']})
                    break
    return pointNodes

#point = {'p': '3', 'v': False, 'd': 1000}
#pn = {'f': '0', 't': '1', 'd': 4}

def setDistanceToNearbyNodes(pf,pn):
    for node in pn:
        pt = [d for d in pl if d['p'] == node['t']][0]
        dtc =  pf['d']+node['d']
        if pt['d'] > dtc:
            pt['d'] = dtc
dest = [d for d in pl if d['p']== end][0]
while dest["v"] == False:
    point = getCurrPoint()
    pointNodes = getNodes(point)
    setDistanceToNearbyNodes(point,pointNodes)
    point['v'] = True


for x in pl:
    print(x)