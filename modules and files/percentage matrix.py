import numpy as np

def convert(a):
    a = a.astype(float)
    for i in range(len(a)):
        total = sum(a[i])

        for j in range(a.shape[1]):
            
            a[i][j] /= total

    return a

print(convert(np.arange(0, 9).reshape(3, 3)))