a = float(input())
x = a
y = (x + a / x) / 2
while abs(y ** 2 - a) >= 0.0000001:
    y = (y + a / y) / 2
print(round(y, 4))
