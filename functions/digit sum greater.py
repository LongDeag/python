def digit_sum_greater(a, b):
    total_a = 0
    total_b = 0
    for i in range(len(str(a))):
        total_a += int(str(a)[i])

    for i in range(len(str(b))):
        total_b += int(str(b)[i])

    if total_a > total_b:
        return "YES"
    return "NO"
