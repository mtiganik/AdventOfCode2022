def checkCycle(cycle):
    if cycle in impCycles:

        cycleval = cycle* X
        impCycleVals.append(cycleval)
        # txt = "cycle occured, val is {}, X is {}"
        # print(txt.format(cycleval, X))

f = open("day10.txt")
impCycles = [20,60,100,140,180,220]
impCycleVals=[]
#f = ["noop", "addx 3", "addx -5"]

cycle = 1
X = 1
for x in f:
    if "noop" in x:
        cycle = cycle +1
        checkCycle(cycle)
    else:
        cycle = cycle +1
        checkCycle(cycle)
        val = int(x.split()[1])
        X = X + val
        cycle = cycle +1
        checkCycle(cycle)

sum = 0
for x in impCycleVals:
    sum = sum + x
print("Sum is: ", sum)