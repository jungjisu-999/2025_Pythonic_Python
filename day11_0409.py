# numpy package(2/3)

import numpy as np

seq_lin = np.linspace(0, 1, 10)

print('(1) make linear sequence:')
print('seq_lin)=', seq_lin )
print('type(seq_lin) =', type(seq_lin))
print('seq_lin[3:8] =', seq_lin[3:8])

mat = np.array([ [ x**n for n in range(5)] for x in range(1,4)])
print(mat)
print(mat[2:1])
print( mat[2:,1:3]) # 질문
print(mat.T)   # 질문 : T가 mat의 attribute인지 / __setattr__ / class때 배울 예정

# A.T : A에는 T라는 attribute가 정의 되어 있다.
# attribute : 함수 name이다.

mat[:2,1:4] = np.array( [ [10,20,30], [-10,-20,-30]])
#Or, mat[:2,1:4] = [[ 10,20,30], [-10,-20,-30]]
print(mat)
if type(mat) == list:
    print('(4) mat is a list.')
else:
    print('(5) mat is not a list: type(mat)=', type(mat))

