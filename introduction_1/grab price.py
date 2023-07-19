distance = float(input())
speed = float(input())
price = 0
if distance == 0:
    price = 0
elif distance != 0:
    price = 12_000

    if distance > 2:
        price += 3_500 * (distance -2)

    if distance > 2:
        price += (distance -2) / speed * 350

print(round(price))
