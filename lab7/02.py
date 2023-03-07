x = int(input("Enter a number: "))
x1 = x
str = ""
if x > 0 and x <=26:
    i = 0
    while i < x:
        j = 0
        while j < x1:
            ascii = chr(65)
            str += chr(ord(ascii)+(j))
            j += 1
        print(str)
        str = ""
        x1 -= 1
        i += 1
else:
    print("Invalid input, program terminates.")
