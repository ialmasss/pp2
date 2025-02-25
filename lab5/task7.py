import re

def to_upper(match):
    return match.group(1).upper()

s = input("input text: ")

camel_case = re.sub(r'_([a-z])', to_upper, s)

print("CamelCase:", camel_case.capitalize())
