def P1FindStr():
    f = open("day3.txt")
    result = ""
    for x in f:
        chars = list(x)
        sack1, sack2 = chars[:len(chars)//2], chars[len(chars)//2:]
        share =  list(set(sack1).intersection(sack2))
        result = result + share[0]
    return result

def P2FindStr():
    f = open("day3.txt")
    result = ""
    for x in f:
        in1 = x.rstrip()
        in2 = f.readline().rstrip()
        in3 = f.readline().rstrip()
        cm = ''.join(set(in1).intersection(in2).intersection(in3))
        result = result + cm
    return result

def getCount(input):
    res = 0
    for x in input:
        if ord(x) < 91:
            res = res + ord(x) - 38
        else:
            res = res + ord(x) - 96
    return res


print("Part1: ", getCount(P1FindStr()))
print("Part2: ", getCount(P2FindStr()))
