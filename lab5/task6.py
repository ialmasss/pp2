import re

s = input("input text: ")

n = re.sub(r"[ ,.]", ":", s)

if n:
    print(n)
else:
    print("no match")