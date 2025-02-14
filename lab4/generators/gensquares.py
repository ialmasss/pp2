a = int(input("Input A: "))
b = int(input("Input B: "))

def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

print(*squares(a, b), sep = ', ' )