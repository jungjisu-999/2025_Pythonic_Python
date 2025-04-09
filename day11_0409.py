# numpy package(1/3)

import numpy as np

matA = [ [1,2,3], [-1,0,1], [0,1,1] ] # 3*3 matrix
matB = [ [1,1,1], [1,1,-2], [5,0,1] ]

u_vec = [-1,1,2] # 1*3 matrix
v_vec = [1,-3,0]

#numpy array from numeric list
u_vec_np = np.array(u_vec)
v_vec_np = np.array(v_vec)

matA_np = np.array(matA)
matB_np = np.array(matB)

print('(1) u_vec_np =', u_vec_np, 'v_vec_np =', v_vec_np)
print('(addition) u_vec_np + v_vec_np =', u_vec_np + v_vec_np)
print('(scalar multiplication) 0.5*matA_np =', 0.5**u_vec_np)

print( '(2-A) matA_np\n', matA_np )
print( '(2-B) matB_np\n', matB_np )
print('(addition) matA_np + matB_np\n', matA_np + matB_np)
print('(scalar multiplication) matA_np matB_np\n', 0.5*matA_np)

print('(matrix multiplication) matA_np matB)np\n', matA_np@matB_np)

inv_matA_np = np.linalg.inv( matA_np )
print('(matrix inverse) the inverse matrix of matA_np\n', inv_matA_np)
print('(confirm inverse) matA_np inv_matB_np\n', matA_np@inv_matA_np)