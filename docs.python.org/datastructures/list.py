l1=[1,2,3]
l1.append(4)
l1[len(l1):]=[5]
print(l1)
l1.extend([6,7])
print(l1)
l1.insert(len(l1),8)
l1.insert(len(l1),9)
print(l1)
l1.remove(9)
l1.pop(l1.index(8))
print(l1)
l2 = l1[:]
l3 = l1.copy()
print(l2,l3)
l2.clear()
del l3[:]
print(l2,l3)
l4=[2,2,2]
print(l4.count(2))
l4 = l1[:]
l4.reverse()
print(l4)
l5=[{'name':'zzz'},{'name':'ff'},{'name':'ll'},{'name':'aa'},{'name':'uu'}]
l5.sort(key=lambda x:x['name'])
print(l5)
l5.sort(key=lambda x:x['name'],reverse=True)
print(l5)



