NM = input("").split(" ")
height = int(NM[0])
width = int(NM[1])

wall = []
for j in range(width):
    wall.append(input(""))

k = int(input())
wallCopy = wall.copy()
for kIndex in range(k):
    text = input()
    for wallIndex in range(len(wall)):
        if text in wall[wallIndex]:
            wallCopy[wallIndex] = wallCopy[wallIndex].replace(text, "*")
wallCopy.reverse()
wallCpTwo = wallCopy.copy()
temp = wallCopy.copy()
for wallCpIndex in range(len(wallCopy)):
    if "*" in wallCopy[wallCpIndex]:
        for wallTextIndex in range(len(wallCopy[wallCpIndex])):
            if wallCopy[wallCpIndex][wallTextIndex] == "*":
                for x1 in range(len(wallCopy)):
                    if x1 != wallCpIndex:
                        if wallCopy[x1][wallTextIndex] != "*":
                            x = wallCopy[x1][wallTextIndex]
                            temp[wallCpIndex] = wallCopy[wallCpIndex].replace("*", x, 1)
                            wallCopy[x1] = wallCopy[x1].replace(str(x), "*", 1)
                            break

temp.reverse()
for i in temp:
    print(i)