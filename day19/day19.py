import re
from queue import Queue
grid = []
f = open("day19/day19.txt")
for x in f:
    grid.append([int(s) for s in re.findall(r'\b\d+\b', x)])


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
    try:
        if int(pattern[pi]) == i: return True
        else: return False
    except IndexError:
        return False

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
            if checkPattern(pattern, patternIndex,3):
                patternIndex = patternIndex +1
            else:
                print("on minute",time, "buy geo machine")

        for i in range(3,-1,-1):
            if checkResCnt(i,data,currRes) and machines[i] < setup[i] and checkPattern(pattern, patternIndex,i):
                currRes = buyMachine(i, currRes, data)
                machines[i] = machines[i] +1
                boughtMachineThisTurn[i] = True
                patternIndex = patternIndex +1
                print(txtToDebug.format(time+1, nameOfMachine[i]))
        
        for i in range(0,4):
            if boughtMachineThisTurn[i]: 
                currRes[i] = currRes[i] + machines[i]-1
                boughtMachineThisTurn[i] = False
            else:
                currRes[i] = currRes[i] + machines[i]
        # print("We have now:",currRes)
        # print(" ")
    return [currRes,patternIndex]

nameOfMachine = ["ore", "clay", "obsidian","geode"]
txtToDebug = "on minute {} buy {} machine"

#PatternFactory
def base_convert(i, b):
    result = []
    while i > 0:
            result.insert(0, i % b)
            i = i // b
    return result
def isValidPattern(pattern,maxValPattern):
    # if len(pattern) > 0:
    #     if not pattern.startswith(maxValPattern):
    #         return False
    if "1" not in pattern: return False
    elif "2" not in pattern: return False
    elif pattern.find('1') > pattern.find('2'): return False
    elif "3" in pattern and pattern.find('2') > pattern.find('3'):
        return False
    elif pattern[1:2]=="3":
        return False
    elif pattern.startswith("0") and pattern[1:2] == "2":
        return False
    elif pattern.startswith("3") or pattern.startswith("2"):
        print(pattern, "should not reach here")
    
    return True



class PatternFactory:
    def __init__(self,strlen, maxValPattern):
        self.strlen = strlen
        self.maxValPattern = maxValPattern
    
    index = 0
    patternsToSkip = []
    def getPattern(self):
        while 1:
            val = ("".join(map(str,base_convert(self.index,4))))
            if len(val) < self.strlen:
                val = "0"*self.strlen + val
                val = val[-self.strlen:]
            if val.startswith("1") and val[1:2] == ("3"):
                return -1
            self.index = self.index + 1
            if isValidPattern(val,self.maxValPattern):break

        return val

# val = 1000000
# print(base_convert(val,4))
# val = val + 4*4*4*4*4 + 4*4*4*4
# print(base_convert(val,4))

i = 0
data = grid[1]
print(data)

maxValPatterns = []
pattern = "0111212223"
result = checkGeodeCnt(data, pattern)

# pattern = "1112123333"
# result = checkGeodeCnt(data, pattern)
for i in range(3,6):
    pf = PatternFactory(i,maxValPatterns)
    maxVal= 0
    while True:
        pattern = pf.getPattern()
        if pattern == -1: break
        result = checkGeodeCnt(data, pattern)
        val, patternIndex = result[0],result[1]
        #print(pattern,"cnt:", val[3], val[0:3] )
        if val[3] >= maxVal:
            maxVal = val[3]

            maxValPatterns.append(pattern) 
    print("i = ", i," maxVal: ", maxVal, "pattern:", maxValPatterns[i])

