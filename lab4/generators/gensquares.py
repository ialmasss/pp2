n = int(input("Input N: "))

def gensquares(n):
    squares = []
    for i in range(n + 1):
        squares.append(i ** 2)
    return squares

print(gensquares(n))