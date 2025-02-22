import re

s = input("input text: ")

n = re.findall(r"\ba[a-z]*b\b", s)

if n:
    print(n)
else:
    print("no match")