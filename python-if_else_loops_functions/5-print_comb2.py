#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print("0{}, ".format(i),end="")
    if i >= 10 and i < 99:
        print("{}, ".format(i),end="")
    if i == 99:
            print(i)
