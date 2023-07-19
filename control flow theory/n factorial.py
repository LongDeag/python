num = int(input())


def factorial(n):
    factorial = 1
    if n < 0:
        print("These does not exist factorial for this number.")
    elif n == 0:
        factorial = 1
        print(factorial)
    elif n > 0:
        for i in range(1, n + 1):
            factorial *= i
        print(factorial)


factorial(num)
