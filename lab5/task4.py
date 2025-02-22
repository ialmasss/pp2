import re

s = input("input text: ")

n = re.findall(r"\b[A-Z][a-z]+\b", s)

if n:
    print(n)
else:
    print("no match")