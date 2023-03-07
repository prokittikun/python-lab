c = int(input())
count = 0
x = 1
while x <= c:
    j = 1
    while j <= c:
        if j < x:
            j += 1
            continue
        if ((x ** 2) + (j ** 2)) == c**2:
            count += 1
        j += 1
    x += 1

print(count)