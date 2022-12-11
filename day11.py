import math
def getWorryLev(item, Operation, divideBy):
    returnVal = item
    if Operation.count("old") == 2 and "*" in Operation:
        returnVal = returnVal * returnVal
        return int(returnVal/divideBy)
    ls=Operation.split()
    num = int(ls[2])
    if "*" in Operation:
        returnVal = returnVal * num
    elif "+" in Operation:
        returnVal = returnVal + num
    return int(returnVal / divideBy)
data= []

f = open("day11.txt")

for x in f:
    monkey = int(x.split()[1].replace(":",""))
    nl = f.readline()
    itemsStr = nl.split()[2:]
    items =[]
    for k in itemsStr:
        k = k.replace(",","")
        items.append(int(k))
    nl = f.readline()
    operation = nl.split("=")[1].strip()
    nl = f.readline()
    divisibleBy = int(nl.split()[3])
    nl = f.readline()
    ifTrue = int(nl.split()[5])
    nl = f.readline()
    ifFalse = int(nl.split()[5])
    f.readline()
    Do = {"Monkey": monkey, "items": items, "Operation": operation, 
    "DivisibleBy": divisibleBy, "ifTrue": ifTrue, "ifFalse":ifFalse, "inspectionCnt": 0,
    "ifFalseCnt":0}
    data.append(Do)

#Part 1
# cycles = 20
# divideBy = 3

#Part 2
cycles = 20
divideBy = 1

dummy = 0
for i in range(0,cycles):
    dummy = i
    for x in data:
        monkeyNo = x["Monkey"]
        items = x["items"]
        Operation = x["Operation"]
        for k in items:
            newLevel = getWorryLev(k, Operation, divideBy)
            if (newLevel/x["DivisibleBy"]).is_integer():
                newLevel = newLevel/x["DivisibleBy"]
                newMonkeyNo = x["ifTrue"]
            else:
                newMonkeyNo = x["ifFalse"]
                if Operation.count("old") == 2 and "*" in Operation:
                    newLevel = math.sqrt(newLevel)
                elif "*" in Operation:
                    ls=Operation.split()
                    num = int(ls[2])

                #x["ifFalseCnt"] = x["ifFalseCnt"] +1
            x["inspectionCnt"] = x["inspectionCnt"] +1
            newMonkey = data[newMonkeyNo]
            newMonkey["items"].append(newLevel)
        x["items"] = []

#After round1:
for x in data:
    txt = "Monkey {}, inspected {} times, have items {}"
    print(txt.format(x["Monkey"],x["inspectionCnt"], x["items"]))