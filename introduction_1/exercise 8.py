import math
from tabulate import tabulate

a = float(input())
result = math.sqrt(a)

dict = [[1, a, abs(a - result)]]


def my_sqrt():
    step = 2
    x = a
    y = (x + a / x) / 2
    dict.append([2, y, abs(y - result)])
    while abs(y ** 2 - a) >= 0.0000001:
        y = (y + a / y) / 2
        step = step + 1
        dict.append([step, y, abs(y - result)])


my_sqrt()

print(dict)

table = tabulate(dict, headers=["Step", "Value", "Difference"])
print(table)
