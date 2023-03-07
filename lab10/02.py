original = []
sum = 0
def accum_sum(l):
    x = original[l]
    return x

while True:
    n = int(input("Enter a number (0 to end): "))
    if n == 0:
        break
    elif n > 0 and n <= 999:
        original.append(n)
    else:
        print("Number is out of range.")
        continue
print("Original list:")
print(original)
print("Accumulative Sum:")
for i in range(0, len(original)):
    sum += accum_sum(i)
    print(sum)
