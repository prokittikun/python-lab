nList = []
i = -1
while True:
    n = int(input())
    if n == -1: break
    if nList == [] or nList[i] <= n:
        nList.append(n)
        i += 1
print(nList)
