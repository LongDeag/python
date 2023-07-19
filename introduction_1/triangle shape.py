n = int(input())
for i in range(n):
    print((n-i-1)*'_' + '/' + 2*i*' ' + '\\' + (n-i-1)*'_')
