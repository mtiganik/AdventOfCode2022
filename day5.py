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
#del slines[0]
K = "_"
N = 4
for x in slines:
    res = ''.join(ele if idx % N or idx == 0 else K for idx, ele in enumerate(x))
    res = res[1:]
    res = res.replace("   ", "[0]")
    res = res.replace("[","").replace("]","").replace(" ", "")
    res = res.split("_")
    stacks.append(res)

for x in stacks:
    print(x)
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
input = open("day5.txt")
#input = ["move 4 from 1 to 9"]

#input = ["move 3 from 3 to 7"]
#input = ["move 1 from 2 to 1", "move 3 from 1 to 3"]
#input = ["move 3 from 3 to 7", "move 4 from 1 to 9"]
for x in input:
    if not "move" in x: continue
    x = x.split(" ")
    move, str,end ,  = int(x[1]), int(x[3]), int(x[5])
    strCnt = getStackLen(str)
    endCnt = getStackLen(end)
    for i in range(0,move):
        val = stacks[strCnt][str-1]
        stacks[strCnt][str-1] = "0"
        strCnt = strCnt -1
        if endCnt == len(stacks) -1:
            addNewLine(end, val)
        else:
            stacks[endCnt+1][end-1] = val
        endCnt = endCnt +1
    # txt = "startStack has {}, end stack has {} crates"
    # print(txt.format(strCnt,endCnt))

print("Result:")
for x in stacks:
    print(x)
