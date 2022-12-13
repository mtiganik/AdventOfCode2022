import ast

pairs = []
left, right = "",""
f = open("day13.txt")
for x in f:
    left,right = x.rstrip(), f.readline().rstrip()
    pair = [left, right]
    pairs.append(pair)
    f.readline()
count = 0

#-1: continue
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

index = 0
for x in pairs:
    index = index +1
    l, r = ast.literal_eval(x[0]), ast.literal_eval(x[1])
    count = count + compare(l,r)*index

print(count)
