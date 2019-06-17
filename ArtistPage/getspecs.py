import os

#var folderLocations = [[50,20],[35,25],[10,20],[20,51],[-20,60],[20,15]];
def removeTrash(l):
    for el in l:
        if el == ".DS_Store":
            l.remove(el)
    return l

#creates a json string of the files in the folder specified
def formFileTree(folder,path): #add quotes to values
    str = "\""+folder+"\""+": {"
    fileList = removeTrash([file for file in os.listdir(path+folder+"/")])
    actFiles = [];
    for file in fileList:
        if "." in file:
            actFiles.append(file)
        else:
            str = str + formFileTree(file,path+folder+"/") + ","
    str = str + "\"files\": ["
    for file in actFiles:
        str = str + "\"" + file + "\"" + ","
    if len(actFiles) != 0:
        str = str[:-1]
    str = str + "]"
    return str + "}\n"

tree = "var fileTree = {" + formFileTree("portfolio","./") + "};"
folders = "var folders = [\"Home\", \"Creators\", \"Store\", \"Projects\"];"
folderLocations = "var folderLocations = [[0,15],[-10,35],[-15,55],[20,30]];"

f = open('specs.js', 'w')
f.write(folders + "\n")
f.write(folderLocations + "\n")
f.write(tree + "\n")
f.close()
