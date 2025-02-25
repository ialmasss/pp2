import re

s = input("input text: ")

n = re.sub(r'([a-z])([A-Z])', r'\1 \2', s)

print(n)