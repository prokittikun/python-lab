hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))

if hours >= 0 and minutes >= 0 and minutes < 60 and hours < 24:
    
    result = (hours*60)+minutes
    if result <= 15:
        print("No charge, thanks.")
    elif result > 15 and result <= 120:
        print("Total amount due is 10 Bahts.")
    else:
        result2 = ((math.ceil(result/60)-2)*10)+10
        print(f"Total amount due is {result2} Bahts.")
else :
    print("Input Error!")