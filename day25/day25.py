f = open("day25/day25.txt")

def toDecimals(inp):
    lenght = len(inp)
    sum = 0
    for i,x in enumerate(inp):
        pow = 5**(lenght-i-1)
        if x == "2": sum = sum + 2*pow
        elif x == "1": sum = sum + pow
        elif x == "0": continue
        elif x == "-": sum = sum - pow
        elif x == "=": sum = sum -2*pow
    return sum

sum = 0
for x in f:
    sum = sum + toDecimals(x.rstrip())

#25/2 = 12,5
def toSnafu(val):
    pow = 21
    snafu = ""
    while True:
        powVal = 5**pow
        if abs(val) < powVal/2:
            snafu = snafu + "0"
        elif val > powVal/2 and val < powVal + powVal/2:
            snafu = snafu + "1"
            val = val - powVal
        elif val > powVal + powVal/2 and val < 2*powVal + powVal/2:
            snafu = snafu +"2"
            val = val -2*powVal
        elif -val < (powVal+ powVal/2) and -val > (powVal - powVal/2):
            snafu = snafu + "-"
            val = val + powVal
        elif -val < (2*powVal + powVal/2) and -val > (2*powVal - powVal/2):
            snafu = snafu + "="
            val = val + 2*powVal
            
        pow = pow -1
        if pow < 0: return snafu

print(sum)
print(toSnafu(sum))
