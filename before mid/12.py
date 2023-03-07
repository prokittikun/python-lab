round = 0
i = 0
target = 0
while True:
    x = int(input())
    y = int(input())
    if x <= 0 or x > 6 or y <= 0 or y > 6:
        print("ERROR")
        continue
    else:
        round += 1
        sum = 0
        sum += x + y
        word = ""
        if sum == 7 or sum == 11: word = "W"
        elif sum == 2 or sum == 3 or sum == 12: word = "L"
        elif i == 0:
            target = sum
            i += 1
            continue
        if sum == target: word = "W"
        if sum == target or target == 0:
            print(f"{round} {sum} {word}")
            break