player1 = int(input("Enter a target (4-digit integer): "))
player2 = int(input("Enter your guess (4-digit integer): "))
p1Clone,p3Clone = player1,player1
p2Clone,p4Clone = player2,player2
position = 0
digit = 0
i = 0
while i < 4:
    x = p1Clone % 10
    p1Clone = p1Clone // 10
    while True:
        y = p2Clone % 10
        p2Clone = p2Clone // 10
        if x == y:
            position += 1 
            break
        else:
            break
    i += 1
i = 0
while i < 4:
    x = p3Clone % 10
    p3Clone = p3Clone // 10
    p4Clone = player2
    i2 = 0
    while True:
        y = p4Clone % 10
        p4Clone = p4Clone // 10
        if x == y:
            digit += 1
        i2 += 1
        if i2 > 3: break
    i += 1
digit = digit - position
if position == 4 and digit == 0:
    print("Congratulations, you just mastered my mind!!")
else:
    if position == 4:
        print("Four positions correct, ", end="")
    elif position == 3:
        print("Three positions correct, ", end="")
    elif position == 2:
        print("Two positions correct, ", end="")
    elif position == 1:
        print("One position correct, ", end="")
    elif position == 0:
        print("No positions correct, ", end="")

    if digit == 4:
        print("four digits correct")
    elif digit == 3:
        print("three digits correct")
    elif digit == 2:
        print("two digits correct")
    elif digit == 1:
        print("one digit correct")
    elif digit == 0:
        print("no digits correct")