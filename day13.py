import ast

def getPart1DataModel(file):
    pairs = []
    left, right = "",""
    f = open(file)
    for x in f:
        left,right = x.rstrip(), f.readline().rstrip()
        pair = [left, right]
        pairs.append(pair)
        f.readline()
    return pairs

def compare(l,r):
    lgt = len(l) if len(l) < len(r) else len(r)
    for i in range(0,lgt):
        if type(l[i]) is int and type(r[i]) is int:
            if l[i] == r[i]: continue
            if l[i] < r[i]: return 1
            if l[i] > r[i]: return 0
        if type(l[i]) is list and type(r[i]) is list:
            rval = compare(l[i],r[i])
            if rval == -1: continue
            else: return rval
        if type(l[i]) is list and type(r[i]) is int:
            rval = compare(l[i],[r[i]])
            if rval == -1: continue
            else: return rval
        if type(l[i]) is int and type(r[i]) is list:
            rval = compare([l[i]],r[i])
            if rval == -1: continue
            else: return rval    
    if len(l) > len(r): 
        return 0
    elif len(l) < len(r): 
        return 1 
    else: return -1

def p1Calculation(pairs):
    count = 0
    index = 0
    for x in pairs:
        index = index +1
        l, r = ast.literal_eval(x[0]), ast.literal_eval(x[1])
        count = count + compare(l,r)*index
    return count


def getPart2DataModel(input):
    packs = [[[2]], [[6]]]
    f = open(input)
    for x in f:
        packs.append(ast.literal_eval(x.rstrip()))
        packs.append(ast.literal_eval(f.readline().rstrip()))
        f.readline()
    return packs

def sortP2(packs):
    for i in range(0,len(packs)-1):
        for j in range(i+1,len(packs)):
            if compare(packs[i], packs[j])==0:
                temp = packs[i]
                packs[i] = packs[j]
                packs[j] = temp
    return packs

def getP2Value(packs):
    i1,i2 = 0,0
    for i in range(0,len(packs)):
        if packs[i] == [[2]]:
            i1 = i+1
        if packs[i] == [[6]]:
            i2 = i+1
    return i1 * i2


file = "day13.txt"

print("Part 1:", p1Calculation(getPart1DataModel(file)))
print("Part 2:", getP2Value(sortP2(getPart2DataModel(file))))