#!/usr/bin/env python3
def print_last_digit(number):
    if number % 10 == 0:
        last = 0
    if number > 0:
        last = (number % 10)
    if number < 0:
        last = (-1 * number) % 10
    print(last, end="")
    return last
