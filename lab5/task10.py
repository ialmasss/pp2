import re

s = input("input text: ")

snake_case = re.sub(r'([A-Z])', r'_\1', s).lower()

print("snake case:", snake_case)