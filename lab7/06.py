height = int(input("Enter height: "))
width = int(input("Enter width: "))

if height <= 0 or width <= 0:
    print("Invalid input, program terminates.")
else:
    i = 0
    while i < height:
        if i % 2 != 0:
            x = 0
            while x < width:
                print(' *',end='')
                x+=1  
        else:
            x = 0
            while x < width:
                print('* ',end='')
                x+=1          
        print()
        i+=1