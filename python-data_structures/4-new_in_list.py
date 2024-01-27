#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    i = 0
    copy = []
    while i < len(my_list):
        copy.append(my_list[i])
        i += 1
    if idx < 0:
        return copy
    elif idx > len(copy):
        return copy
    else:
        copy[idx] = element
    return copy
