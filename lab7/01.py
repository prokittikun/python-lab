x = int(input("Enter a number: "))
str = ""
if x > 0 and x <=26:
    i = 0
    while i < x:
        ascii = chr(65)
        str += chr(ord(ascii)+i)
        print(str)
        i += 1
else:
    print("Invalid input, program terminates.")
