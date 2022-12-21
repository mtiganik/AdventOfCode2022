def calculate(val1,val2, op):
    if op == "*": return val1*val2
    elif op == "+": return val1+val2
    elif op == "-": return val1-val2
    elif op == "/": return int(val1/val2)
    else: print("shouldnt reacht here")

def backwardCalc(v1,op,v2,targetVal):
    if type(v1) == int:
        if op == "+": return targetVal - v1
        if op == "*": return targetVal/v1
        if op == "-": return v1 - targetVal  
        if op == "/": return v1 / targetVal
    elif type(v2) == int:
        if op == "+": return targetVal-v2
        if op == "*": return targetVal/v2
        if op == "-": return targetVal + v2
        if op == "/": return targetVal * v2


f = open("day21/day21.txt")

data = []
root = 0
humn = 0
for x in f:
    curr = x.rstrip().split(":")
    name, op = curr[0].strip(), curr[1].strip()
    nd = {"name":name}
    if op.isdigit():
        od = {"calc":True, "val":int(op)}
    else:
        op = op.split()
        od = {"calc":False,"el1":op[0],"el1calc":False,"el2":op[2],"el2calc":False, "op":op[1]}
    nd.update(od)
    if nd["name"] == "root": root = nd
    if nd["name"] == "humn": humn = nd
    data.append(nd)
print("elements read")
print("calculating")
while(root["calc"]==False):
    for x in data:
        if x["calc"] == True: continue
        else: 
            for y in data:
                if y["calc"]==True:
                    if x["el1"]==y["name"]:
                        x["el1calc"] = y["val"]
                    elif x["el2"] == y["name"]:
                        x["el2calc"] = y["val"]
                    if type(x["el1calc"]) == int and type(x["el2calc"]) == int:
                        x["calc"] = True
                        x["val"] = calculate(x["el1calc"], x["el2calc"], x["op"])
                   

def addElementToStack(newval,currCheck):
    if newval["el1"] == currCheck["name"]:
        result = {"n": newval["name"], "v1":newval["el1"],"op":newval["op"],"v2":newval["el2calc"]}
    elif newval["el2"] == currCheck["name"]:
        result = {"n": newval["name"], "v1":currCheck["val"],"op": newval["op"], "v2": newval["el2"]}
    else:
        print("shouldnt reach here")
        return 0
    return result


print("calculating done")

print(root["val"])


print("root val1:", root["el1calc"], "val2:", root["el2calc"])

currCheck = humn
stack = []
while currCheck != root:
    # checkcnt = 0
    for x in data:
        if "el1" in x:
            if x["el1"] == currCheck["name"] or x["el2"] == currCheck["name"]:
                stack.append(addElementToStack(x, currCheck))
                currCheck = x
stack.reverse()
stackRoot = stack[0]

valToGet = root["el1calc"] if type(stack[0]["v1"]) == int else root["el2calc"]
stack[0]["val"] = valToGet

print(valToGet)
for i in range(1,len(stack)):
    targetVal = stack[i-1]["val"]
    stack[i]["val"] = backwardCalc(stack[i]["v1"], stack[i]["op"], stack[i]["v2"],targetVal)


for x in stack:
    print(x["n"], x["v1"], x["op"], x["v2"], x["val"])

print("Part2:", stack[len(stack)-1]["val"])
