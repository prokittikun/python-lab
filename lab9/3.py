def nb_year(p0, percent, aug, p):
    day = 0
    while p0 < p:
        p0 = p0 + p0 * (percent/100) + aug
        day += 1
    return day
print( nb_year(1000, 2, 30, 1150) )