list1=[1,2,3,4,5]
print(list1)
list1.append('sdsdsd')
print('after update',list1)

list2=[2,3,4,5,10,2,3,23]
list1.extend(list2)
print('after list2 update:',list1)

list1.sort()
print('sorted:')
print(list1)

list1.insert(2,22222)
print(list1)

print (sorted(list2,key=lambda x:x%2))
