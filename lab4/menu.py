print("---<< Main Menu >>---")
print("    <B>urger Meal")
print("    <C>hicken Meal")
print("    <P>asta Meal")
choice = input("Enter your choice: ")

if choice == "b" or choice == "B":
    print("---<< Burger Sub Menu >>---")
    print("    <R>egular Burger")
    print("    <C>heese Burger")
    print("    <D>ouble Cheese Burger")
    subChoice = input("Enter your choice: ")
    if subChoice == "r" or subChoice == "R":
        print(f"Your Regular Burger is 60 Baht.")
    elif subChoice == "c" or subChoice == "C":
        print(f"Your Cheese Burger is 75 Baht.")
    elif subChoice == "d" or subChoice == "D":
        print(f"Your Double Cheese Burger is 90 Baht.")
    else:
        print("Invalid sub menu choice.")
elif choice == "c" or choice == "C":
    print("---<< Chicken Sub Menu >>---")
    print("    <F>ried Chicken")
    print("    <G>rilled Chicken")
    print("    <C>hef's Chicken")
    subChoice = input("Enter your choice: ")
    if subChoice == "f" or subChoice == "F":
        print(f"Your Fried Chicken is 120 Baht.")
    elif subChoice == "g" or subChoice == "G":
        print(f"Your Grilled Chicken is 150 Baht.")
    elif subChoice == "c" or subChoice == "C":
        print(f"Your Chef's Chicken is 180 Baht.")
    else:
        print("Invalid sub menu choice.")
elif choice == "p" or choice == "P":
    print("---<< Pasta Sub Menu >>---")
    print("    <S>paghetti de Italiano")
    print("    <L>asagna Supreme")
    print("    <M>acaroni Special")
    subChoice = input("Enter your choice: ")
    if subChoice == "s" or subChoice == "S":
        print(f"Your Spaghetti de Italiano is 90 Baht.")
    elif subChoice == "l" or subChoice == "L":
        print(f"Your Lasagna Supreme is 120 Baht.")
    elif subChoice == "m" or subChoice == "M":
        print(f"Your Macaroni Special is 100 Baht.")
    else:
        print("Invalid sub menu choice.")
else:
    print("Invalid main menu choice.")
    exit()