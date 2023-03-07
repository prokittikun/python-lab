print("Enter variables and values:")
dic = {}
variables = []
programList = []
while True:
    var = input()
    x = var.split("=")
    if var != "-1":
        dic[x[0].strip()] = int(x[1].strip())
    else:
        break
print("Enter your program:")
while True:
    program = input()
    if program == "-1":
        break
    pSplit = program.split("=")
    if len(pSplit) > 1: 
        dic[pSplit[0].strip()] = pSplit[1].strip()
    programList.append(program)
print("Result:")
def cvPrint(text):
    key = list(dic.keys())
    new = ""
    for i in range(len(text)):
        if text[i] not in "{}":
            if text[i] in key and (text[i-1] == "{" or text[i+1] == "}"):
                new += str(dic[text[i]])
            else:
                new += text[i]
    return new

for i in range(len(programList)):
    ans = cvPrint(programList[i])
    print(ans)
