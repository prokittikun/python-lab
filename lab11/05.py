test = input()
criterion = input()
listV = []
passed = 0
percentage = 0.0
for i in range(len(test)):
    if test[i] != "[" and test[i] != "]":
        listV.append(test[i])
criterionArr = list(criterion)
for i in listV:
    if i in criterionArr:
        passed += 1
print(passed)
if len(listV) == 0: print("0.00")
else:
    print(f"{passed/len(listV)*100:.2f}")