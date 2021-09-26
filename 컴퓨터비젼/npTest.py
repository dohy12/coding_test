import numpy as np

x, y = np.meshgrid(np.linspace(-1,1,5), np.linspace(-1,1,5))

print(x)
print(y)

print(2**3)

d = np.sqrt(x*x + y*y)
print(d)

sigma = 1.0

g = np.exp(-((d)**2/(2.0*sigma**2)))

print(g)