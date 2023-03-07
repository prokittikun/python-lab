hours = int(input("Enter number of hour: "))
minutes = int(input("Enter number of minutes: "))
if hours >= 0 and minutes >= 0 :
    if hours * 60 + minutes > 15 :
        if hours == 2 and minutes == 0 : pass
        print(f"Total amount due is {hours * 10} Bahts.")
    else : 
        print("No charge, thanks.")