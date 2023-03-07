n = int(input())
banknoteArr = []
for i in range(0,n):
    banknote = int(input())
    banknoteArr.append(banknote)
changeCount = int(input())
banknoteArr.sort(reverse=True)
changeOutput = []
frequency = []
for x in range(len(banknoteArr)):
    divide = changeCount // banknoteArr[x]
    bankCount = banknoteArr[x] * divide
    changeCount = changeCount - bankCount
    changeOutput.append(banknoteArr[x])
    frequency.append(divide)
for k in range(len(changeOutput)):
    print(f"{changeOutput[k]}: {frequency[k]}")
