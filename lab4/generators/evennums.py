n = int(input("Input N: "))

def even(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i

print(*even(n), sep = ', ')