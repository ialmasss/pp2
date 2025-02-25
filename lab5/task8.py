import re

s = input("input text: ")

n = re.findall(r'[A-Z][a-z]*', s)

print(n)