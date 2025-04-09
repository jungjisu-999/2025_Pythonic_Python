# numpy more(3/3)

import numpy as np

matA = np.array([[0,2], [2,3]])
print('matrix -->\n ', matA)

# eigenvalue-eigenvector of mat
result = np.linalg.eig( matA)

print('(1) result type -->', type(result))
print('result = ', result)
print('(2) eigenvalue: ', result.eigenvalues)
print('(3) eigenvalue:', result[0])
print('(4) eigenvalue:', result.eigenvectors)
print('(5) eigenvector:', result[1])

#singular value decomposition : 머신러닝, 통계학과에서 자주 사용
matB = np.array([[0,2], [2,3], [1,1]])
print('matrix -->\n ', matB)
result = np.linalg.svd( matB)
print('(6) result type --> ', type(result))
print('result =', result)
U = result.U
S = result.S
Vh = result.Vh
print('U -->\n', U)
print('S = ', S)
print('Vh -->\n', Vh)

#Sigma matrix
m,n = matB.shape
Sigma = np.zeros(n*m).reshape(m,n)
sub = np.diag( S )
Sigma[:len(S), :len(S)] = sub
print('Sigma -->\n', Sigma)
print('U Sigma Vh -->\n', U@Sigma@Vh)

# x,y = 3,4 : 튜플 unpacking
# x,y = [3,4] : unpacking


