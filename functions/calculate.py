def calculate( n ):
    a0 = 0
    a1 = 1

    if n == 0:
        return a0
    elif n == 1:
        return a1
    else:
        a2 = 0
        for i in range(2, n+1):
            a2 = 2*a1+a0
            a0 = a1
            a1 = a2
        return a2

