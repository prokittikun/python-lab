digit = int(input())
if digit >= 0:
    sum = 0
    answer = 0
    while True:
        n = digit % 10
        digit = digit // 10
        sum += n
        answer = sum
        if digit == 0: break
    if sum >= 10:
        while True:
            if sum < 10: answer = 0
            n = sum % 10
            sum = sum // 10
            sum += n
            if answer == 0: break
    print(sum)    