def getWorryLev(item, Operation):
    returnVal = item
    if Operation.count("old") == 2 and "*" in Operation:
        returnVal = returnVal * returnVal
        return int(returnVal/3)
    ls=Operation.split()
    num = int(ls[2])
    if "*" in Operation:
        returnVal = returnVal * num
    elif "+" in Operation:
        returnVal = returnVal + num
    return int(returnVal / 3)
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
    "DivisibleBy": divisibleBy, "ifTrue": ifTrue, "ifFalse":ifFalse, "inspectionCnt": 0}
    data.append(Do)

# for x in data:
#     print(x)
#Data object:
# data = [{"Monkey":0, "items":[79,98], "Operation":"old * 19", 
# "DivisibleBy": 23, "ifTrue": 2, "ifFalse":3, "inspectionCnt": 0},
# {"Monkey":1, "items":[54,65,75,74], "Operation":"old + 6", 
# "DivisibleBy": 19, "ifTrue": 2, "ifFalse":0, "inspectionCnt": 0},
# {"Monkey":2, "items":[79,60,97], "Operation":"old * old", 
# "DivisibleBy": 13, "ifTrue": 1, "ifFalse":3, "inspectionCnt": 0},
# {"Monkey":3, "items":[74], "Operation":"old + 3", 
# "DivisibleBy": 17, "ifTrue": 0, "ifFalse":1, "inspectionCnt": 0},]


dummy = 0
for i in range(0,20):
    dummy = i
    for x in data:
        monkeyNo = x["Monkey"]
        items = x["items"]
        Operation = x["Operation"]
        for k in items:
            newLevel = getWorryLev(k, Operation)
            if (newLevel/x["DivisibleBy"]).is_integer():
                newMonkeyNo = x["ifTrue"]
            else:
                newMonkeyNo = x["ifFalse"]
            x["inspectionCnt"] = x["inspectionCnt"] +1
            newMonkey = data[newMonkeyNo]
            newMonkey["items"].append(newLevel)
        x["items"] = []

#After round1:
for x in data:
    txt = "Monkey {}, inspected {} times, have items {}"
    print(txt.format(x["Monkey"],x["inspectionCnt"], x["items"]))