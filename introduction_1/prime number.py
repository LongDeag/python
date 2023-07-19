n = int(input())


def is_prime(c):
    if c <= 1:
        return False
    else:
        for i in range(2, c):
            if c % i == 0:
                return False

        return True


print(is_prime(n))

if not is_prime(n):
    print("not prime")
else:
    print("prime")
