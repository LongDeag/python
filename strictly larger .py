arr = list(map(int, input().split()))
L =[]

for index in range(1, len(arr)):
    if arr[index] > arr[index-1]:
        L.append(arr[index])
if L == []:
    print("NONE")
else:
    print(' '.join(str(item) for item in L))

