random_number = int(input())
def odd_positive(n):
    for i in range(n-1 ,0, -1):
        if i % 2 != 0:
            print(i)

odd_positive(random_number)
