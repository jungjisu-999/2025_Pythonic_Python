#List / mutable
#my_list_setitem.py

L = ['a', 'b', 'c', 'd', 'e']

print('L =', L )

L[1:2] = [1,2,3]
print('L =', L)

L[5:] = [10,20,30]
print('L =', L)

L[2:4] = ['apple', 'mango', 'lemon']
print('L =', L)