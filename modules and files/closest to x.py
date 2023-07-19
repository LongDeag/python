import random

size = int(input())
arr = list(map(int, input().split()))[:size]
x = int(input())

f = lambda i: abs(i-x)
arr_new = list(map(f, arr))

L = []

for i in range(size):
    if arr_new[i] == min(arr_new):
        L.append(arr[i])

print(random.choice(L))
