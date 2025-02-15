import math

n = int(input("Number of sides: "))
l = float(input("Length of a side: "))
f = (n * l*l) / 4 * math.tan(math.pi / n)

print("Area of a regular polygon:", round(f))