m = int(input())
n = int(input())


def friendly(a, b):
    total_a = 0
    total_b = 0
    for i in range(1, a):

        if a % i == 0:
            total_a += i
    for i in range(1, b):

        if b % i == 0:
            total_b += i

    if b == total_a and a == total_b:
        return "YES"
    return "NO"


