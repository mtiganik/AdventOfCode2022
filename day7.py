input = open("day7.txt")
f = {"main": {}, "size": 0}
input.readline()
input.readline()
currFolder = "main"
for x in input:
    if x.startswith("$ cd"):
        if ".." in x:
            path = currFolder.split("/")
            path.pop()
            currFolder = '/'.join(path)
        else:
            newFolder = x.split()[2]
            currFolder = currFolder + "/" + newFolder
    elif "$ ls" not in x:
        path = currFolder.split("/")
        element = {}
        key, value = "", ""
        if "dir" in x:
            key, value = x.replace("dir ", "").strip(), {}
        if x[0].isdigit():
            file = x.split()
            key, value = file[1], int(file[0])
        element = f
        for y in path:
            element = element[y]
        element[key] = value


def folderSearch(folder):
    for y in folder:
        if type(folder[y]) is int and "size" not in y:
            folder["size"] = folder["size"] + folder[y]
        if type(folder[y]) is dict:
            newFolder = folder[y]
            newFolder["size"] = 0
            folder["size"] = folder["size"] + folderSearch(newFolder)
    return folder["size"]
main = f["main"]

folderSearch(f)
used = f["size"]
total = 70000000
available = total - used
needed = 30000000 - available
print("needed: ", needed)

part2Result = 30000000
def findfolderToDelete(folder):
    global part2Result
    for y in folder:
        if "size" in y:
            if folder[y] > needed and folder[y] < part2Result:
                part2Result = folder[y]
        if type(folder[y]) is dict:
            newFolder = folder[y]
            findfolderToDelete(newFolder)

part1result = 0
def folderSizeMeas(folder):
    global part1result
    for y in folder:
        if "size" in y:
            if folder[y] <= 100000:
                print(folder[y])
                result = result + folder[y]
        if type(folder[y]) is dict:
            newFolder = folder[y]
            folderSizeMeas(newFolder)
            
folderSizeMeas(f)
print(part1result)

findfolderToDelete(f)       
print(part2Result)

