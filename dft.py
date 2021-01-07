import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.fft import fft

def dft(x):
	print(fft(x))
	print("***********")
	N = len(x)
	sumtot = 0
	j = complex(0,1)
	for i in range(0, N-1):
		sum = (x[i])*np.exp(-2*j*np.pi*1*i/N)
		print(sum)
		sumtot = sumtot+sum
	return sumtot



#a= 10
t = np.linspace(0, 0.02, 10)
y = np.sin(2*np.pi*50*t)

#print(y)
print("*****************")
print(dft(y))

plt.plot(t,y)
plt.show()
