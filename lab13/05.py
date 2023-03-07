def fibonacci(n):
    i = 1
    f1 = 1
    f2 = 1
    next = 0
    if n == 0 or n == 1:
        return 1
    else:
        while i < n:
            next = f1 + f2
            f1 = f2
            f2 = next
            i += 1
        return next

n = input()
text = input()
sum = 0
ErrMsg = False

i = 0
if text != " " and text != "" and n.isnumeric():
    n = int(n)
    while i <= n:
        if text in "Ee": #Even
            if i % 2 == 0:
                sum += fibonacci(i)
        elif text in "Oo": #Odd
            if n == 0:
                ErrMsg = True
            else:
                if i % 2 != 0:
                    sum += fibonacci(i)
        else:
            ErrMsg = True
        i += 1
else:
    ErrMsg = True

if ErrMsg:
    print("ERROR")
else:
    print(sum)
