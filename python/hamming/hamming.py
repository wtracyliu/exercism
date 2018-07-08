def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('different length ')
    length_list = [len(set(i)) for i in list(zip(strand_a, strand_b))]
    print(length_list)
    if 2 in length_list:
        return length_list.count(2)
    else:
        return 0

