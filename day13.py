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

def compare(l,r):
    lgt = len(l) if len(l) < len(r) else len(r)
    txt = "compare {} vs {}"
    print(txt.format(l,r))
    for i in range(0,lgt):
        txt = "compare {} vs {}"
        print(txt.format(l[i],r[i]))
        if type(l[i]) is int and type(r[i]) is int:
            if l[i] == r[i]: 
                continue
            if l[i] < r[i]: 
                txt = "left side is smaller so inputs are in right order"
                print(txt)
                return 1
            if l[i] > r[i]: 
                txt = "right side is smaller so inputs are not in right order"
                print(txt)
                return 0
        if type(l[i]) is list and type(r[i]) is list:
            # txt = "{} is list and {} is list"
            # print(txt.format( r[i]))
            return compare(l[i],r[i])
        if type(l[i]) is list and type(r[i]) is int:
            txt = "Mixed types, convert right to {} and retry comparison"
            print(txt.format( [r[i]]))
            return compare(l[i],[r[i]])
        if type(l[i]) is int and type(r[i]) is list:
            txt = "Mixed types, convert left to {} and retry comparison"
            print(txt.format( [l[i]]))
            return compare([l[i]], r[i])
    
    if len(l) > len(r): 
        txt = "len {} is bigger then {}, return 0"
        print(txt.format(len(l), len(l)))
        return 0
    else: 
        txt = "we return 1"
        print(txt.format(len(l), len(l)))

        return 1 

index = 0
for x in pairs:
    index = index +1
    l, r = ast.literal_eval(x[0]), ast.literal_eval(x[1])
    count = count + compare(l,r)*index

print(count)
