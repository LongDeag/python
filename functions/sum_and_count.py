def sum_and_count(inp):
    sum_list = list()
    cn_list = list()
    for tup in inp:
        if type(tup) == int:
            sum_list.append(tup)
            cn_list.append(tup)
        else:
            sum_list.append(sum(tup))
            cn_list.append(len(tup))
    return sum_list, cn_list


inp = ((1,2,5), (3,7,5,10), (1))
sum_list, cnt_list = sum_and_count(inp)
print(*sum_list)
print(*cnt_list)