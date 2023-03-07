import math
hours = int(input('Enter number of hours (0-20): '))
minutes = int(input('Enter number of minutes (0-59): '))
buyAmt = int(input('Enter shopping amount: '))
if hours >= 0 and hours <= 20 and minutes >= 0 and minutes <= 59:
    hourMinutes = (hours * 60)+ minutes
    if hourMinutes > 1200:
        print("Invalid time.")
    else:
        freeHour = 0
        if buyAmt >= 300 and buyAmt <= 3000:
            freeHour = 2
        if hourMinutes <= 120 or buyAmt >= 3001: # (hourMinutes >= 180 and hourMinutes <= 240 and buyAmt >= 300 and buyAmt <= 3000) or
            print("No charge, thank you.")
        elif hourMinutes >= 180 and hourMinutes <= 240:
            if buyAmt >= 300 and buyAmt <= 3000:
                print("No charge, thank you.")
            hour = (math.ceil(hourMinutes/60) // 2)
            print(f"Total amount due is {hour*20} Baht, thank you.")
        elif hourMinutes >= 240:
            hour = ((math.ceil(hourMinutes/60)-2)) - freeHour  
            if freeHour == 2:
                print(f"Total amount due is {(hour*50)} Baht, thank you.")
            else:
                hourTwoThree = (math.ceil(hourMinutes/60)-2)-2
                print(f"Total amount due is {(hourTwoThree*50)+(40)} Baht, thank you.")
else:
    print("Invalid time.")
    
    