import re

s = input("input text: ")

n = re.findall(r"ab{2,3}", s)

if  n:
    print(n)
else:
    print("no match")