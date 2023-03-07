number = int(input("Enter a number: "))
if number < 0:
    print("Invalid input, program terminates.")
else:
    i = 0
    while i < number + 1:
        print(f"{i}! = ",end="")
        if(i == 0): print(f"1 = 1")
        total = 1
        x1 = 0
        while x1 < i:
            total *= (x1+1)
            print(f"{i - x1}",end="")
            x1 += 1
            if x1 < i: 
                print(" x ",end="")
            else:
                print(" ",end="")
        if(i != 0): print(f"= {total}")
        i += 1