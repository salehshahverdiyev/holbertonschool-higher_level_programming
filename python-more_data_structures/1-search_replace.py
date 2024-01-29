#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    i = 0
    while i < len(my_list):
        if my_list[i] == search:
            new.append(replace)
        else:
            new.append(my_list[i])
        i += 1
    return new
