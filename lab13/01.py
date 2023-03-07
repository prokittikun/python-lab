def namelist(names):
    newName = ""
    for i in range(len(names)):
        newName += names[i]
        if i+1 == len(names)-1: newName += " & "
        elif i != len(newName)-1: newName += ", "
    return newName[0:len(newName)-2]
print( namelist([]) == '' )