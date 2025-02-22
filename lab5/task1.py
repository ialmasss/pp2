import re 

s = input("input text: ")

n = re.findall(r"a.*b", s)

if n:
    print(n)
else:
    print("no match")