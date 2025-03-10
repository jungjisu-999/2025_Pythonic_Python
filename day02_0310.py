# 모든게 전부 object.
# 모든 변수 이름을 attribute다.
#numpy --> 수치해석학
#matplot --> 눈으로 확인할 때 그림용.
# numpy안에 통계처리 패키지도 있음.
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,500) # 0하고 5를 포함해서 50개로 쪼개줘라
y = np.exp(-x)*np.sin(2*np.pi*x)

plt.plot(x,y)
plt.show()












