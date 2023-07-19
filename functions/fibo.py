def fibo(n):
    if n < 2:
        f = n
    else:
        f = fibo(n-1) + fibo(n-2)
    return f
print(fibo(6))