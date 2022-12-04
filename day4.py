def areOverlaps(i1,i2):
    s1 = set(i1)
    s2 = set(i2)
    if len(s1.intersection(s2)) > 0:
        return(True)
    return(False)
def getNumbs(input):
    numbs = list(input.split('-'))
    start, end = int(numbs[0]), int(numbs[1])
    res = []
    for i in range(start, end+1):
        res.append(i)
    return res

def fullyContainsAnother(i1,i2):
    i1s, i1e = i1[0], i1[len(i1)-1]
    i2s, i2e = i2[0], i2[len(i2)-1]
    if i1s <= i2s and i1e >= i2e:
        return True
    if i1s >= i2s and i1e <= i2e:
        return True
    return False

f = open("day4.txt")
FulloverLapCnt = 0
SomeoverLapCnt = 0
for x in f:
    pair = x.split(',')
    e1 = getNumbs(pair[0])
    e2 = getNumbs(pair[1].strip())
    
    if(fullyContainsAnother(e1,e2)):
        FulloverLapCnt = FulloverLapCnt +1
    if(areOverlaps(e1,e2)):
        SomeoverLapCnt = SomeoverLapCnt +1

print("Part1: ", FulloverLapCnt)
print("Part2: ", SomeoverLapCnt)