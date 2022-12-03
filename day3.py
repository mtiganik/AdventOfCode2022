# def getPriority(x):
#     return ord(x)


f = open("day3.txt")
result = ""
for x in f:
    chars = list(x)
    sack1, sack2 = chars[:len(chars)//2], chars[len(chars)//2:]
    share =  list(set(sack1).intersection(sack2))
    result = result + share[0]
    #result.append(share)

res = 0
for x in result:
    if ord(x) < 91:
        res = res + ord(x) -38
        
    else:
        res = res + ord(x) - 96
    # txt = str(x) +":" + str(res)
    # print(txt)

print(res)
# priorities = 0
# print(ord('a'))
# for x in result:
#     priorities = priorities + ord(chr(x))
#     txt =x + ": " + ord(chr(x))
#     print(txt)