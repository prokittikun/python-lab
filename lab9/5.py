def fibo(n):
    i = 1
    First_Value = 0
    Second_Value = 1
    Next = 0
    while (i <= n):
        if (i <= 1):
            Next = i
        else:
            Next = First_Value + Second_Value
            First_Value = Second_Value
            Second_Value = Next
        i = i + 1
    return Next


n = int(input("Enter n: "))
print("{} {}".format(n, fibo(n)))
