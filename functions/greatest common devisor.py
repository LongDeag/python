def GCD(a, b):
    GCD = 1
    for gcd in range(1, a + b):
        if a % gcd == 0 and b % gcd == 0:
            GCD = gcd
    return GCD


print(GCD(756, 360))
