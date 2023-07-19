import math


def vector_distance(v1, v2, norm='euclidean'):
    if norm == 'manhattan':
        result = sum(abs(x - y) for x, y in zip(v1, v2))

    elif norm == 'cosine':
        tu_so = sum(x * y for x, y in zip(v1, v2))
        mau_so = math.sqrt(sum(x * x for x in v1)) * math.sqrt(sum(y * y for y in v2))
        result = (tu_so / mau_so)

    else:
        result = math.sqrt(sum((x - y) ** 2 for x, y in zip(v1, v2)))

    return round(result, 9)


print(vector_distance([1, 2], [4, 6], norm='manhattan'))
