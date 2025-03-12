# n = int( input('n = '))
n = int( input('칸의개수 = '))
m = int( input('줄의개수 = '))
line1 = '+' + '-'*n + '+' + '-'*n + '+'
line2 = '|' + ' '*n + '|' + ' '*n + '|'


line2enter = line2 + '\n'
lines = line1+ '\n' + line2enter*m + line1 + line2enter*m + line1
print(lines)
# 출력값 이상함.
# \n : enter key string
#Unicode