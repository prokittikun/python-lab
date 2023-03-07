scores = []
i = 0
def find_mode(list):
    mode = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(list)):
        mode[list[i]] += 1
    modeCount = []
    max2 = max(mode)
    for x in range(len(mode)):
        if max2 == mode[x]:
            max2 = mode[x]
            modeCount.append(x)
    return modeCount
while i < 20:
    score = int(input("Enter score: "))
    if score >= 0 and score <= 10:
        scores.append(score)
        i += 1
    else:
        print("Score is out of range.")
        continue
print("-----")
print("Original list:")
print(scores)
print("Mode of scores:")
mode = find_mode(scores)
for j in range(0,len(mode)):
    print(mode[j])