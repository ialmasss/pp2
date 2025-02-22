import re

s = input("input text: ")

n = re.findall(r"ab*", s)

if n:
    print(n)
else:
    print("no match")