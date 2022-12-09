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
ih,jh, it,jt = 0,0,0,0


for x in f:
    x = x.split(" ",1)
    dirc, steps = x[0], int(x[1])
    for k in range(0,steps):
        if dirc == "R":
            if jh == len(grid[0])-1:
                addRight(ih,grid,"H")
                addRight(0,tail,".")
            else:
                grid[ih][jh+1] = "H"
            grid[ih][jh] = "."
            jh = jh +1
        if dirc == "L":
            if jh == 0:
                addLeft(ih,grid,"H")
                addLeft(0,tail,".")
                grid[ih][jh+1] = "."
                jt = jt +1
            else:
                grid[ih][jh-1] = "H"
                grid[ih][jh] = "."
                jh = jh - 1
        if dirc == "U":
            if ih == 0:
                addUp(jh,grid,"H")
                addUp(0,tail,".")
                grid[ih+1][jh] = "."
                it = it +1
            else:
                grid[ih-1][jh] = "H"
                grid[ih][jh] = "."
                ih = ih-1
        if dirc == "D":
            if ih == len(grid) -1:
                addDown(jh,grid,"H")
                addDown(0,tail,".")
            else:
                grid[ih+1][jh]="H"
            grid[ih][jh] = "."
            ih = ih+1 
        
        ## Tail Setup
        #Right
        if jh - jt == 2:
            grid[it][jt] = '.'
            it = ih
            jt = jt+1
            grid[it][jt] = 'T'
            tail[it][jt] = "#"
        #Down
        elif ih-it == 2:
            grid[it][jt] = "."
            jt=jh
            it = it+1
            grid[it][jt] = "T"
            tail[it][jt] = "#"
        #Left
        elif jh - jt == -2:
            grid[it][jt] ="."
            it = ih
            jt = jt-1
            grid[it][jt] = "T"
            tail[it][jt] = "#"
        #Up
        elif ih - it == -2:
            grid[it][jt] = "."
            jt = jh
            it = it-1
            grid[it][jt] = "T"
            tail[it][jt] = "#"

        # print("Round")
        # for x in grid:
        #     print(x)
    # print(steps)
    #if "R" in x:
for x in tail:
    str = ""
    str.join(x)
    print(x)
cnt = 0
for x in tail:
    cnt = cnt + x.count("#")
print(cnt)