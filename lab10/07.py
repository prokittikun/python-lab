exercise = int(input())
percentage = float(input())
student = int(input())
scorePerStudent = []
count = 0

def calPercentage(i, score):
    str = ""
    if score < percentage:
        str = f"({i+1}) {score:.2f}"
    else:
        str = f"{i+1} {score:.2f}"
    return str
i = 0
while i < student:
    score = int(input())
    scorePerStudent.append(((score*100)/exercise))
    if scorePerStudent[i] < percentage:
        count += 1
    i += 1
print(count)
for x in range(0, len(scorePerStudent)):
    print(calPercentage(x, scorePerStudent[x]))
