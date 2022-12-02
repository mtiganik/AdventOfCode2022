def part2():
    f = open("day2.txt")

    total = 0
    for x in f:
        line = x.split()
        if line[0] == "A":
            if line[1] == "X":
                total = total + 3
            if line[1] == "Y":
                total = total + 4
            if line [1] == "Z":
                total = total + 8
        if line[0] == "B":
            if line[1] == "X":
                total = total + 1
            if line[1] == "Y":
                total = total + 5
            if line [1] == "Z":
                total = total + 9
        if line[0] == "C":
            if line[1] == "X":
                total = total + 2
            if line[1] == "Y":
                total = total + 6
            if line [1] == "Z":
                total = total + 7

    print(total)

def part1():
    f = open("day2.txt")

    total = 0
    for x in f:
        line = x.split()
        if line[0] == "A":
            if line[1] == "X":
                total = total + 4
            if line[1] == "Y":
                total = total + 8
            if line [1] == "Z":
                total = total + 3
        if line[0] == "B":
            if line[1] == "X":
                total = total + 1
            if line[1] == "Y":
                total = total + 5
            if line [1] == "Z":
                total = total + 9
        if line[0] == "C":
            if line[1] == "X":
                total = total + 7
            if line[1] == "Y":
                total = total + 2
            if line [1] == "Z":
                total = total + 6

    print(total)

part1()
part2()