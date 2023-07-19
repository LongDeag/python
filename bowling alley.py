N, K = map(int, input().split())
result = [x for x in (N*'I')]


for times in range(K):
    left_kn, right_kn = map(int, input().split())
    for i in range(left_kn, right_kn+1):
        result[i-1] = '.'


print(''.join(result))
