number = int(input("Enter positive integer: "))
x = 2
if number <= 0:
    print("Invalid number.")
while x <= number:
    if number % x == 0:
        print(x)
        number /= x
        x = 2
        continue
    x += 1