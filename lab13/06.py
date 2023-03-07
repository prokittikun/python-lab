list = []

def check_order(l):
    if l == []: return "The list is empty."
    if similar(l):
        return "The list is in non-increasing and non-decreasing order."
    if increase(l):
        return "The list is in non-decreasing order."
    if decrease(l):
        return "The list is in non-increasing order."
    if increase(l) == False and decrease(l) == False and len(l) != l.count(l[1]):
        return "The list is in random order."

def similar(l):
    last_value = l[0]
    for i in range(1, len(l)):
        if last_value == l[i]:
            last_value = l[i]
        else:
            return False
    return True

def increase(l):
    min = 0
    increase = 0
    for i in range(len(l)):
        if min == 0 or min <= l[i]:
            min = l[i]
            increase += 1
    if increase == len(l):
        return True
    else:
        return False

def decrease(l):
    min = 0
    decrease = 0
    for i in range(len(l)):
        if min == 0 or min >= l[i]:
            min = l[i]
            decrease += 1
            continue
    if decrease == len(l):
        return True
    else:
        return False

while True:
    n = int(input("Enter a number (-1 to end): "))
    if (n < -1 or n > 100): 
        print("Number is out of range.")
        continue
    if n == -1:
        print("-----")
        print("Original list:")
        print(list)
        break
    list.append(n)
 
print(check_order(list))
