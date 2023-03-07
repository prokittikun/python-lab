print("First fraction:")
numerator1 = int(input(">>Enter a numerator a: "))
denominator1 = int(input(">>Enter a denominator b: "))
print("Second fraction:")
numerator2 = int(input(">>Enter a numerator c: "))
denominator2 = int(input(">>Enter a denominator d: "))
numerator = (numerator1 * denominator2) + (numerator2 * denominator1)
denominator = denominator1 * denominator2
print("Summation of the two fractions is {} / {}".format(numerator, denominator))
