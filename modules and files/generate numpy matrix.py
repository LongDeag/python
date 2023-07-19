import numpy as np

a = np.arange(1, 21)
a = a.reshape(5, 4)
for i in range(1, 6):
    a[i-1] = np.arange(i, 21, 5)

print(a.reshape(4,5))
