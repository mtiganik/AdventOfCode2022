def GetStartStacks():
    f = open("day5.txt")
    slines = []
    for x in f:
        if x == '\n': break
        x = " " + x
        slines.append(x.strip('\n'))
    slines.reverse()
    first = slines[0].strip()
    first = ' '.join(first.split())
    first = first.split(" ")
    stacks = []
    K = "_"
    N = 4
    for x in slines:
        res = ''.join(ele if idx % N or idx == 0 else K for idx, ele in enumerate(x))
        res = res[1:]
        res = res.replace("   ", "[0]")
        res = res.replace("[","").replace("]","").replace(" ", "")
        res = res.split("_")
        stacks.append(res)
    return stacks


def getStackLen(index):
    for i in range(0,len(stacks)):
        if stacks[i][index-1] == '0': 
            return i -1
    return len(stacks)-1

def addNewLine(end, val):
    line = []
    for x in range(0, len(stacks[0])):
        line.append("0")
    line[end-1] = val
    stacks.append(line)

def solvePart2(stacks):

    input = open("day5.txt")
    for x in input:
        if not "move" in x: continue
        x = x.split(" ")
        move, str,end ,  = int(x[1]), int(x[3]), int(x[5])
        strCnt = getStackLen(str)
        endCnt = getStackLen(end)
        for i in range(0,move):
            val =stacks[strCnt-move+i+1][str-1]
            stacks[strCnt-move+i+1][str-1] = "0"
            if endCnt+i == len(stacks) -1:
                addNewLine(end, val)
            else:
                stacks[endCnt+1+i][end-1] = val
    return stacks

def getResult(stacks):
    res = ""
    for i in range(0, len(stacks[0])):
        for j in range(0, len(stacks)):
            if j+1 == len(stacks): return 0
            if stacks[j+1][i] == "0": 
                res = res + stacks[j][i] 
                break 
    return res

stacks = GetStartStacks()
stacks = solvePart2(stacks)
result = getResult(stacks)
print(result)
# print("Result:")
# for x in stacks:
#     print(x)
