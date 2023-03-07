size = input().split("x")
p = int(input())
bom = []
y = []
def replacer(s, newString, index):
    if index < 0:  
        return newString + s
    if index > len(s):  
        return s + newString
    return s[:index] + newString + s[index + 1:]
yTemp = []
for pIndex in range(p): 
    bom.append([input()])
for yCreate in range(int(size[1])):
    y.append("0" * int(size[0]))
# plant spike
for yIndex in range(len(y)):
    for xIndex in range(len(y[yIndex])):
        for bIndex in range(len(bom)):
            xy = bom[bIndex][0].split(",")
            if yIndex == int(xy[1]):
                # print(y[yIndex][xIndex])
               y[yIndex] = replacer(y[yIndex], "*", int(xy[0]))
print(y)
# y =8, x =10
