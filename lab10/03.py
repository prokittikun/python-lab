import math
scores = []
count = 0
# standard deviation


def find_sd(l):
    average = sum(scores)/count
    return ((scores[l]-average)**2)/(count-1)


while True:
    score = float(input("Enter score: "))
    if score == -1:
        break
    elif score >= 0 and score <= 100:
        count += 1
        scores.append(score)
    else:
        print("Score is out of range.")
        continue
result = 0
for i in range(0, count):
    result += find_sd(i)
if scores != []:
    print(f"Maximum score is {max(scores):.2f}.")
    print(f"Minimum score is {min(scores):.2f}.")
    print(f"Average score is {sum(scores)/count:.2f}.")
    print(f"Standard deviation is {math.sqrt(result):.2f}.")
