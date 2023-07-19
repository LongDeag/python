x = int(input())


def gt(n):
    giai_thua = 1
    for number in range(1, n+1):
        giai_thua *= number
    return giai_thua


def pascal_triangle(k):
    for row in range(0, k + 1):
        result = ""
        for he_so in range(0, row + 1):
            result = result + ' ' + str(round(gt(row)/gt(he_so)/gt(row-he_so)))
        print(result)


pascal_triangle(x)
