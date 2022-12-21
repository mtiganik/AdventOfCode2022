def calculate(val1,val2, op):
    if op == "*": return val1*val2
    elif op == "+": return val1+val2
    elif op == "-": return val1-val2
    elif op == "/": return int(val1/val2)
    else: print("shouldnt reacht here")


f = open("day21/day21.txt")

data = []
val ={"name":"fdsfsd", "calc": False,"val":"","op":"pppw + sjmn" }
root = 0
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
    data.append(nd)

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
                    

print(root)
print("root calc found")
