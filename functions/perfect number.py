def is_perfect(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    print(divisors)
    if sum(divisors) == n:
        print(f"{n} is perfect.")
    else:
        print(f"{n} is not perfect")


is_perfect(28)
