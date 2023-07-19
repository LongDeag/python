def sum_of_digit(n):
    result = 0
    if n != 0:
        result = n % 10 + sum_of_digit(int(n/10))
    return result

print(sum_of_digit(152))