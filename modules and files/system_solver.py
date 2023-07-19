import numpy as np

a = np.array([
    [1, 3, -2, 5],
    [3, 5, 6, 7],
    [2, 4, 3, 8], 
], dtype = 'float')

# m is the number of rows
m = a.shape[0] 
# n is the number of columns
n = a.shape[1]

def reduce_matrix():
    b = np.copy(a).astype(float)

    for time in range(1, m):
        for i in range(time, m):
            for j in range(time-1,n):
                a[i,j] = a[time-1,j] * (-b[i,time-1]/a[time-1,time-1]) + a[i,j]
        b = np.copy(a).astype(float)

reduce_matrix()

b = np.copy(a).astype(float)
print(b)

    
A = a[:, :n-1]
print(A)

B = a[:, 3:]
print(B)

X = np.linalg.dot(A,B)

print(X)