#1
x = {'type' : 'fruit', 'name' : 'apple'}
for y in x.values():
  print(y)

#2
x = {'type' : 'fruit', 'name' : 'apple'}
for y, z in x.items():
  print(y, z)

#3
myset = {'apple', 'banana', 'cherry'}
for x in myset:
  print(x)

#4
x = {'type' : 'fruit', 'name' : 'apple'}
for y in x.keys():
  print(y)