pkmLevel = int(input("Enter level pokemon: "))
pkbLevel = input("Enter level pokeball: ")
distance = int(input("Enter distance: "))

if pkmLevel >= 0 and pkmLevel <= 40:
    if pkbLevel == 'h' or pkbLevel == 'H':
        x = 0.01
        s = 100-(pkmLevel*distance*x)
        if s >= 0.00 and s <= 100.00:
            print(f"{s:.2f} percent.")
        else:
            print(f"0.00 percent.")
    elif pkbLevel == 'm' or pkbLevel == 'M':
        x = 0.03
        s = 100-(pkmLevel*distance*x)
        if s >= 0.00 and s <= 100.00:
            print(f"{s:.2f} percent.")
        else:
            print(f"0.00 percent.")
    elif pkbLevel == 'l' or pkbLevel == 'L':
        x = 0.05
        s = 100-(pkmLevel*distance*x)
        if s >= 0.00 and s <= 100.00:
            print(f"{s:.2f} percent.")
        else:
            print(f"0.00 percent.")
elif pkmLevel >= 41 and pkmLevel <= 60:
    if pkbLevel == 'h' or pkbLevel == 'H':
        x = 0.01
        s = 100-(pkmLevel*distance*x)
        if s >= 0.00 and s <= 100.00:
            print(f"{s:.2f} percent.")
        else:
            print(f"0.00 percent.")
    elif pkbLevel == 'm' or pkbLevel == 'M':
        x = 0.05
        s = 100-(pkmLevel*distance*x)
        if s >= 0.00 and s <= 100.00:
            print(f"{s:.2f} percent.")
        else:
            print(f"0.00 percent.")
    elif pkbLevel == 'l' or pkbLevel == 'L':
        x = 0.03
        s = 100-(pkmLevel*distance*x)
        if s >= 0.00 and s <= 100.00:
            print(f"{s:.2f} percent.")
        else:
            print(f"0.00 percent.")
elif pkmLevel >= 61 and pkmLevel <= 100:
    if pkbLevel == 'h' or pkbLevel == 'H':
        x = 0.01
        s = 100-(pkmLevel*distance*x)
        if s >= 0.00 and s <= 100.00:
            print(f"{s:.2f} percent.")
        else:
            print(f"0.00 percent.")
    elif pkbLevel == 'm' or pkbLevel == 'M':
        x = 0.08
        s = 100-(pkmLevel*distance*x)
        if s >= 0.00 and s <= 100.00:
            print(f"{s:.2f} percent.")
        else:
            print(f"0.00 percent.")
    elif pkbLevel == 'l' or pkbLevel == 'L':
        x = 0.1
        s = 100-(pkmLevel*distance*x)
        if s >= 0.00 and s <= 100.00:
            print(f"{s:.2f} percent.")
        else:
            print(f"0.00 percent.")

