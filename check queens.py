def can_beat(a, b):
    return False if a[0] != b[0] and a[1] != b[1] and abs(a[0] - b[0]) != abs(a[1] - b[1]) else True


def check_queens():
    queens = [list(map(int, input().split())) for i in range(8)]
    for i in range(8):
        for j in range(i + 1, 8):
            if can_beat((queens[i]), (queens[j])):
                return "YES"
    return "NO"


T = int(input())

for x in range(T):
    print(check_queens())