# import os
#
# print('Current working directory -->', os.getcwd())
#
# x = input('string = ')
# print('Congratulations!' , x)

n = int(input('n = '))
line1 = '+' + '-'*n + '+' + '-'*n + '+'
line2 = '|' + ' '*n + '|' + ' '*n + '|'

# print(line1, end='')  # ' ' --> empty string
print(line1)
print(line2)
print(line2)
print(line1)
print(line2)
print(line2)
print(line1)

# 키보드의 모든 키는 문자열이다.
# \n : enter key string
