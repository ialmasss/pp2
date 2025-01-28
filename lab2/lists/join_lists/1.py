#1
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print (list3)

#2
list3 = list1.extend(list2)
print(list3)

#3
list1 = ['a', 'b' , 'c']
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)