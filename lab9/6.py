#Alternating Sum
def alternating_sum(n):
    i = 1
    sum = 0
    while i <= n:
        if i % 2 == 1:
            sum += i
        else:
            sum -= i
        i += 1
    return sum
