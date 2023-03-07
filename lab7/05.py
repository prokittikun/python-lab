# Prime number checker
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        print("End of program, goodbye.")
        break
    elif number <= 1:
        print("Invalid input, try again.")
        continue
    i = 1
    sum = 0
    while i < number:
        if number % i == 0:
            sum += 1
        i += 1
    if sum == 1:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

        
