def reverse( n ):
    m = ""
    for i in range(len(str(n))-1, -1, -1):
        m += str(n)[i]
    return m


def dec_to_bin(n):
    new_number = ""
    while n != 0:
        r = n % 2
        n = n // 2


        new_number += str(r)
    return reverse(new_number)

print(dec_to_bin(112))