list = []

def check_order(l):
    if len(l) == 0:
        return "The list is empty."
    elif len(l) == l.count(l[1]):
        return "The list is in non-increasing and non-decreasing order."
    elif increase(l):
        return "The list is in non-decreasing order."
    elif decrease(l):
        return "The list is in non-increasing order."
    else:
        return "The list is in random order."

def increase(l):
    min = l[0]
    for i in range(1, len(l)):
        if l[i] >= min:
            min = l[i]
            continue
        else:
            return False
    return True


def decrease(l):
    min = l[0]
    for i in range(1, len(l)):
        if min >= l[i]:
            min = l[i]
            continue
        else:
            return False
    return True

while True:
    n = int(input("Enter a number (-1 to end): "))
    if n == -1:
        print("-----")
        print("Original list:")
        print(list) 
        break
    if n < 0 or n > 100 :
        print("Number is out of range.")
        continue
    list.append(n)


print(check_order(list))