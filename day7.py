input = open("day7.txt")
f = {"main": {}}
input.readline()
input.readline()
currFolder = "main"
for x in input:
    # if x[0] == '$':
    #     print("New cmd")
    if x.startswith("$ cd"):
        if ".." in x:
            path = currFolder.split("/")
            path.pop()
            currFolder = '/'.join(path)
            print("folder back: ", currFolder )
        else:
            newFolder = x.split()[2]
            currFolder = currFolder + "/" + newFolder
            print("new folder: ", currFolder)
    if x.startswith("$ ls"):
        print("list items")
    else:
        path = currFolder.split("/")
        prevElement = {}
        element = {}
        for p in path:
            prevElement = element
            element = f[p]  
        if "dir" in x:
            x = x.replace("dir ", "").strip()
            f[x] = {}
        if x[0].isdigit():
            file = x.split()
            f[file[1]] = int(file[0])


#print(f)

f = {"main" : {
"a":{"e": {"i": 584}, "f":29116, "g": 2557, "h.lst": 62596},
"b.txt":14848514, 
"c.dat": 8504156, 
"d":{"j":4060174,"d.log": 8033020,"d.ext":5626152,"k": 7214296, } }}

print(f["main"]["a"]["e"]["i"])

def folderSearch(folder):
    for y in folder:
        if type(folder[y]) is int:
                #BL here
            print(folder[y])
        if type(folder[y]) is dict:
            newFolder = folder[y]
            folderSearch(newFolder)
main = f["main"]

folderSearch(main)
