#!/usr/bin/python3
def uniq_add(my_list=[]):
    i = 0
    j = 0
    summ = 0
    new = []
    while i < len(my_list):
        if my_list[i] not in new:
            new.append(my_list[i])
        i += 1
    while j < len(new):
        summ += new[j]
        j += 1
    return summ
