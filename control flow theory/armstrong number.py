for i in range(0, 1000):
    num_length = int(len(str(i)))
    list =[]
    for num_num in range(0, num_length):
        list.append(int(str(i)[num_num])**num_length)
    s = sum(list)
    if s == i:
        print(s)
