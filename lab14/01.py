def count_char(str):
    str = str.lower()
    dic = {}
    for i in str:
        if i.isalpha():
            x = str.split(i)
            count = find(str,i)
            dic[i] = count
    return dic
def find(str,i):
    count = 0
    for x in str:
        if x == i: count += 1
    return count
print(count_char("Hello, There"))