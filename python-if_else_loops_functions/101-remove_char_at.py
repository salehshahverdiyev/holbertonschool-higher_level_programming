#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    a = ""
    while i < len(str):
        if n == i:
            i += 1
            continue
        a += str[i]
        i += 1
    return a
