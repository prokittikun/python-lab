def remove_duplicates(t):
    t2 = []
    for x in t:
        if x not in t2:
            t2.append(x)
    return t2