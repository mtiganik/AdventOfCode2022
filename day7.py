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
    # elif x.startswith("$ ls"):
    #     print("list items")
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



# print(f)

# f = {"main" : {
# "a":{"e": {"i": 584}, "f":29116, "g": 2557, "h.lst": 62596},
# "b.txt":14848514, 
# "c.dat": 8504156, 
# "d":{"j":4060174,"d.log": 8033020,"d.ext":5626152,"k": 7214296, } }}


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

result = 0
def folderSizeMeas(folder):
    global result
    for y in folder:
        if "size" in y:
            if folder[y] <= 100000:
                print(folder[y])
                result = result + folder[y]
        if type(folder[y]) is dict:
            newFolder = folder[y]
            folderSizeMeas(newFolder)
            
folderSizeMeas(f)
print(result)
