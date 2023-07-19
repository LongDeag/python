def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

def print_prime(numbers):
    list = []
    for smaller_prime in range(2, numbers):
        if is_prime(smaller_prime) == True:
            list.append(smaller_prime)
    print(' '.join(str(number) for number in list))

print_prime(8)