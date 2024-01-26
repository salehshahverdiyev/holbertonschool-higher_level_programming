#!/usr/bin/python3
def uppercase(str):
    i = 0
    while i < len(str):
        if 97 <= ord(str[i]) <= 123:
            upper = chr(ord(str[i]) - 32)
        else:
            upper = str[i]
        i += 1
        print("{}".format(upper), end="")
    print()
