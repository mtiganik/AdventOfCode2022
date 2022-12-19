import re
grid = []
# f = open("day19/day19.txt")
# for x in f:
#     grid.append([int(s) for s in re.findall(r'\b\d+\b', x)])


def getSetup(pattern):
    ore = pattern.count("0") +1
    clay = pattern.count("1")
    obs = pattern.count("2")
    geode = pattern.count("3")
    return [ore, clay, obs, geode]


def checkResCnt(i,data,currRes):
    if i == 0:
        if currRes[0] >= data[1]: return True
    if i == 1:
        if currRes[0] >= data[2]: return True
    if i == 2:
        if currRes[0] >= data[3] and currRes[1] >= data[4]: return True
    if i == 3:
        if currRes[1] >= data[5] and currRes[2] >= data[6]: return True
    return False

def buyMachine(i, currRes,data):
    newRes = currRes
    if i == 0:
        newRes[0] = newRes[0] - data[1]
    if i == 1:
        newRes[0] = newRes[0] - data[2]
    if i == 2:
        newRes[0] = newRes[0] - data[3]
        newRes[1] = newRes[1] - data[4]
    if i == 3:
        newRes[0] = newRes[0] - data[5]
        newRes[2] = newRes[2] - data[6]
    return newRes

def checkPattern(pattern, pi,i):
    temp = pattern.split("-")
    if int(temp[pi]) == i: return True
    else: return False

def checkGeodeCnt(data,pattern):
    setup = getSetup(pattern)
    mins = 24
    machines = [1,0,0,0]
    currRes = [0,0,0,0]
    boughtMachineThisTurn = [False,False,False,False]
    patternIndex = 0
    for time in range(0,mins):

        #Try to buy geode allways first:
        if checkResCnt(3,data,currRes):
            currRes = buyMachine(3, currRes, data)
            machines[3] = machines[3] +1
            boughtMachineThisTurn[3] = True
            #print(txtToDebug.format(time+1, nameOfMachine[i]))

        for i in range(0,3):
            if checkResCnt(i,data,currRes) and machines[i] < setup[i] and checkPattern(pattern, patternIndex,i):
                currRes = buyMachine(i, currRes, data)
                machines[i] = machines[i] +1
                boughtMachineThisTurn[i] = True
                patternIndex = patternIndex +1
                #print(txtToDebug.format(time+1, nameOfMachine[i]))
        
        for i in range(0,4):
            if boughtMachineThisTurn[i]: 
                currRes[i] = currRes[i] + machines[i]-1
                boughtMachineThisTurn[i] = False
            else:
                currRes[i] = currRes[i] + machines[i]
        # print("We have now:",currRes)
        # print(" ")
    return currRes[3]

nameOfMachine = ["ore", "clay", "obsidian","geode"]
txtToDebug = "on minute {} we bought {} machine"

# data = grid[0]
# print(grid[0])
# print(grid[1])

data1 = [2, 2, 3, 3, 8, 3, 12]
data1 = [1, 4, 2, 3, 14, 2, 7]

pattern2 = "1-1-1-2-1-2" 
pattern2 = "0-1-1-2-1-2" 
patterns = ["1-1-1-2-1-2-2-3-3"]
patterns = ["111212233"]


maxVal = 0
txt = "with pattern {} we mine {} geos"
for k in patterns:
    val = checkGeodeCnt(data1, k)
    print(txt.format(k, val))
    if val >= maxVal:
        maxVal = val
print("Max:",data1, maxVal)

patterns = [
    "1-1-1-2-2-2-2",
    "1-1-1-2-2-2-1",
    "1-1-1-2-2-1-2",
    "1-1-1-2-1-1-1",
    "1-1-1-1-2-2-2",
    "1-1-1-1-2-2-1",
    "1-1-1-1-2-1-2",
  # "1-1-1-1-1-1-1",
    "1-1-2-1-2-2-2",
    "1-1-2-1-2-2-1",
    "1-1-2-1-2-1-2",
    "1-1-2-1-2-1-1",
    "1-1-2-1-1-2-2",
    "1-1-2-1-1-2-1",
    "1-1-2-1-1-1-2",
  # "1-1-2-1-1-1-1",
    "0-1-1-2-2-2-2",
    "0-1-1-2-2-2-1",
    "0-1-1-2-2-1-2",
    "0-1-1-2-1-1-1",
    "0-1-1-1-2-2-2",
    "0-1-1-1-2-2-1",
    "0-1-1-1-2-1-2",
  # "0-1-1-1-1-1-1",
    "0-1-2-1-2-2-2",
    "0-1-2-1-2-2-1",
    "0-1-2-1-2-1-2",
    "0-1-2-1-2-1-1",
    "0-1-2-1-1-2-2",
    "0-1-2-1-1-2-1",
    "0-1-2-1-1-1-2",
  # "0-1-2-1-1-1-1",
    "1-0-1-2-2-2-2",
    "1-0-1-2-2-2-1",
    "1-0-1-2-2-1-2",
    "1-0-1-2-1-1-1",
    "1-0-1-1-2-2-2",
    "1-0-1-1-2-2-1",
    "1-0-1-1-2-1-2",
  # "1-0-1-1-1-1-1",
    "1-0-2-1-2-2-2",
    "1-0-2-1-2-2-1",
    "1-0-2-1-2-1-2",
    "1-0-2-1-2-1-1",
    "1-0-2-1-1-2-2",
    "1-0-2-1-1-2-1",
    "1-0-2-1-1-1-2",
  # "1-0-2-1-1-1-1",
]
