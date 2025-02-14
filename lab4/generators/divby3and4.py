n = int(input("Input N: "))

def divisible(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

print(*divisible(n), sep = ', ')