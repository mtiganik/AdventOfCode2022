def addFolderSizes(folder):
    for y in folder:
        if type(folder[y]) is int and "size" not in y:
            folder["size"] = folder["size"] + folder[y]
        if type(folder[y]) is dict:
            newFolder = folder[y]
            newFolder["size"] = 0
            folder["size"] = folder["size"] + addFolderSizes(newFolder)
    return folder["size"]


def findfolderToDelete(folder):
    global part2Result
    for y in folder:
        if "size" in y:
            if folder[y] > needed and folder[y] < part2Result:
                part2Result = folder[y]
        if type(folder[y]) is dict:
            newFolder = folder[y]
            findfolderToDelete(newFolder)

def folderSizeMeas(folder):
    global part1result
    for y in folder:
        if "size" in y:
            if folder[y] <= 100000:
                part1result = part1result + folder[y]
        if type(folder[y]) is dict:
            newFolder = folder[y]
            folderSizeMeas(newFolder)

input = open("day7.txt")
f = {"main": {}, "size": 0}
input.readline()
input.readline()
currFolder = "main"

#Get Data Object:
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



addFolderSizes(f)

#Part1:
part1result = 0
folderSizeMeas(f)
print("Part1: ", part1result)

#Part2:
used = f["size"]
total = 70000000
available = total - used
needed = 30000000 - available
part2Result = 30000000
findfolderToDelete(f)       
print("Part2: ", part2Result)

