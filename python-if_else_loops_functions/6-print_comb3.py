#!/usr/bin/python3
for a in range(10):
    for b in range(a + 1, 10):
        if a != b:
            print("{:d}{:d}".format(a, b), end=(", " if a < 8 else "\n"))
