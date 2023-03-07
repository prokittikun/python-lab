data = input().split(",")
newData = []
for i in range(len(data)):
    if i != 0 and i < len(data): newData.append(",")
    newData.append(f"\"{data[i].strip()}\"")
print("".join(newData))