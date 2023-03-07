fileName = input()
cloneFileName = fileName[0:15]
ext = fileName.split(".")
reserved = "\/*:|\"<> "
dot = 0
newName = ""
for i in cloneFileName:
    if( i in reserved): 
        newName += "_"
    elif i == "." and (dot == 0 or dot < cloneFileName.count(".")-1) and (fileName.count(".") != 1):
        newName += "_"
        dot += 1
    else:
        newName += i
tempExt = ext[-1]
tempExtSlice = ""
for x in tempExt:
    if x in reserved: tempExtSlice += "_"
    else: tempExtSlice += x
if "." not in newName and fileName.count(".") == 0: print(newName)
elif newName.count(".") == 1: print(newName)
else: print(f"{newName}.{tempExtSlice[0:3]:}")




