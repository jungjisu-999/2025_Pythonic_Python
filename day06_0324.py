# 30분 지각 monday

import random
lr = [1, -1]
wt = [0.7, 0.3]

n = 100
curr = 0
print('my initial position =', curr)

for k in range( n ):
    curr = curr + random.choices(lr, wt, k=1)[0]
    print( curr)

print('my current position =', curr)