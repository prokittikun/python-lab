n = input()
nReplace = n.replace(",", "")
nAndDec = nReplace.split(".")
nCount = len(nAndDec[0])
number = nAndDec[0]
newNumber = ""
error = 0
if "." in n and len(nAndDec[1]) > 2: error += 1
elif "." in n and len(n.split(".")[0].replace(",", "")) < 4 and "," in n.split(".")[0]: error += 1
elif "." not in n and len(n.replace(",", "")) < 4 and "," in n: error += 1
elif "." in n and nAndDec[1] == "": error += 1
if "," in n and len(nAndDec[0]) > 3:
    x = 4
    while True:
        if x > len(n.split(".")[0]): break
        if n.split(".")[0][-x] != ",": 
            error += 1
            break
        x += 4
for i in range(0,len(nAndDec[0])):
    if number[i] in "1234567890": newNumber += number[i]
    else:
        error += 1
        break
if error == 0 and "." in n: print(f"{int(newNumber)+1}.{nAndDec[1]}")
elif error == 0: print(f"{int(newNumber)+1}")
else: print("ERROR")