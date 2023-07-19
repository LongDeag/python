n = int(input())
print(n)

sequence = [n]

while n != 1:
    if n % 2 == 0:
        n//=2
        sequence.append(n)
    elif n % 2 != 0:
        n = n * 3 + 1
        sequence.append(n)

print(' '.join(str(number) for number in sequence))
