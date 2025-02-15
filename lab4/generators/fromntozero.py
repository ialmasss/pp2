n = int(input("Input N: "))

def zeroton(n):
    for i in range(n, -1, -1):
        yield i

print(*zeroton(n), sep = ', ')