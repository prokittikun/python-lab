textGroup = []
frontOfEqual = []
backOfEqual = []
while True:
    text = input()
    if text == "-1":
        break
    textGroup.append(text)
    frontOfEqual.append(text.split("=", 1)[0].strip())
    backOfEqual.append(text.split("=", 1)[1].strip())
max = ""
for j in textGroup:
    jStrip = j.split("=", 1)[0].strip()
    if max == "" or len(max) < len(jStrip) : max = jStrip
for i in range(len(textGroup)):
    front = textGroup[i].split("=")
    print(" "*(len(max)-len(front[0].strip())) + f"{frontOfEqual[i]} = {backOfEqual[i]}")
