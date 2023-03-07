def check_prime(n):
    i = 1
    count = 0
    while i < n:
        if n % i == 0:
            count += 1
        i += 1
    if count == 1:
        return True
    else:
        return False
print(check_prime(10478))