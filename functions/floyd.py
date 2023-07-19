def floyd(n):
    for i in range(n):
        if i % 2 == 0:
            for j in range(i + 1):

                if j % 2 == 0:
                    print(1, end="")
                else:
                    print(0, end="")
            print("")
        else:
            for j in range(i + 1):
                if j % 2 == 0:
                    print(0, end="")
                else:
                    print(1, end="")
            print("")
