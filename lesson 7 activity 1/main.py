lst = ['apple','corn','banana','dates','fig']

print("length of element:",(len))
print("first element:",lst[0])
print("last element:",lst[-1])

lst.append('guava')
print("update list:", lst)

lst.remove('dates')
print("update list:", lst)

lst.pop(1)
print("update list:", lst)

lst.reverse()
print("reversed list:", lst)

print("multipication list:",lst*2)