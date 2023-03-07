import math
x = float(input("Enter x : "))
answer = 0
if x < 0:
    answer = math.sqrt((x**2) + 1)
elif x == 0:
    answer = x
elif x > 0 and x <= 99:
    answer = (3 * (x**2)) - ((1-x)**2)
else:
    answer = (2*(x**3)) - (x/(math.sqrt(x+1)))
print(f"f({x:.2f}) = {answer}")

