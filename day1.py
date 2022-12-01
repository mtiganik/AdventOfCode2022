f = open("2022-1.txt")
list = [0]
current = 0
for x in f:
    if x != "\n":
        current = current + int(x)
    else: 
        list.append(current)
        current  = 0

list.sort()
for x in list:
    print(x)
