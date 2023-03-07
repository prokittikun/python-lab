def sqrt_n_times(x, n):
    i = 1
    while i <= n:
        x = x**(1/2)
        i += 1
    return x