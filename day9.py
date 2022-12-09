def addRight(pos,g,letter):
    for x in g:
        x.append(".")
    g[pos][len(g[0])-1] = letter

def addDown(pos,g,letter):
    rowToAdd = ["."]*len(g[0])
    rowToAdd[pos] = letter
    g.append(rowToAdd)

def addLeft(pos,g,letter):
    for x in g:
        x.insert(0,".")
    g[pos][0] = letter

def addUp(pos,g,letter):
    rowToAdd = ["."]*len(g[0])
    rowToAdd[pos] = letter
    g.insert(0, rowToAdd)
    
#3x3 grid for start
# grid = [[".",".","."],[".","s","."],[".",".","."]]
# tail = [[".",".","."],[".","s","."],[".",".","."]]
grid = [["s"]]
tail = [["#"]]

f = open("day9.txt")
#f = [ "D 2", "L 3", "D 1"]
ik = [0,0,0,0,0,0,0,0,0,0]
jk = [0,0,0,0,0,0,0,0,0,0]

for x in f:
    x = x.split(" ",1)
    dirc, steps = x[0], int(x[1])
    for k in range(0,steps):
        #first knot:
        if dirc == "R":
            if jk[0] == len(grid[0])-1:
                addRight(ik[0],grid,"H")
                addRight(0,tail,".")
            else:
                grid[ik[0]][jk[0]+1] = "H"
            grid[ik[0]][jk[0]] = "."
            jk[0] = jk[0] +1
        if dirc == "L":
            if jk[0] == 0:
                addLeft(ik[0],grid,"H")
                addLeft(0,tail,".")
                grid[ik[0]][jk[0]+1] = "."
                #jk[1] = jk[1] +1
                jk = [y+1 for y in jk]
                jk[0] = 0
            else:
                grid[ik[0]][jk[0]-1] = "H"
                grid[ik[0]][jk[0]] = "."
                jk[0] = jk[0] - 1
        if dirc == "U":
            if ik[0] == 0:
                addUp(jk[0],grid,"H")
                addUp(0,tail,".")
                grid[ik[0]+1][jk[0]] = "."
                #ik[1] = ik[1] +1
                ik = [y+1 for y in ik]
                ik[0]=0
            else:
                grid[ik[0]-1][jk[0]] = "H"
                grid[ik[0]][jk[0]] = "."
                ik[0] = ik[0]-1
        if dirc == "D":
            if ik[0] == len(grid) -1:
                addDown(jk[0],grid,"H")
                addDown(0,tail,".")
            else:
                grid[ik[0]+1][jk[0]]="H"
            grid[ik[0]][jk[0]] = "."
            ik[0] = ik[0]+1 
        
        ## Tail Setup
        for i in range(1,len(ik)):
            #Right
            if jk[i-1] - jk[i] == 2:
                grid[ik[i]][jk[i]] = '.'
                ik[i] = ik[i-1]
                jk[i] = jk[i]+1
                grid[ik[i]][jk[i]] = "% s" % i
                #tail[it][jt] = "#"
            #Down
            elif ik[i-1]-ik[i] == 2:
                grid[ik[i]][jk[i]] = "."
                jk[i]=jk[i-1]
                ik[i] = ik[i]+1
                grid[ik[i]][jk[i]] = "% s" % i
                #tail[it][jt] = "#"
            #Left
            elif jk[i-1] - jk[i] == -2:
                grid[ik[i]][jk[i]] ="."
                ik[i] = ik[i-1]
                jk[i] = jk[i]-1
                grid[ik[i]][jk[i]] = "% s" % i
                #tail[it][jt] = "#"
            #Up
            elif ik[i-1] - ik[i] == -2:
                grid[ik[i]][jk[i]] = "."
                jk[i] = jk[i-1]
                ik[i] = ik[i]-1
                grid[ik[i]][jk[i]] = "% s" % i
                #tail[it][jt] = "#"
    
        # print("Round")
        # for x in grid:
        #     print(x)
    print("Round")
    for x in grid:
        str = ""
        str = str.join(x)
        print(str)

# str = ""
# list1 = ["a","b","c"]
# str.join(list1)
# print()
# for x in tail:
#     str = ""
#     str = str.join(x)
#     print(str)
# cnt = 0
# for x in tail:
#     cnt = cnt + x.count("#")
# print(cnt)