import math
minutes = int(input("Minutes before due:"))
temperature = float(input("Temperature: "))
raining = input("Is it raining (y/n)? ")

day = math.floor((minutes // 60)/24+0.5) 

if day < 2:
    print(f"{day} days before due.")
    print(f"I will do the assignment.")
elif day >=2 and day <= 5:
    if temperature > 40 or (temperature > 25 and raining == 'y' or raining == 'Y'):
        print(f"{day} days before due.")
        print(f"I will do the assignment.")
    print(f"{day} days before due.")
    print(f"I will do the assignment.")
else:
    print(f">>> {day} days before due.")
    print(f">>> I will not do the assignment.")