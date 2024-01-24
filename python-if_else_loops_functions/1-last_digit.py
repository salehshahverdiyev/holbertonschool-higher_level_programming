#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


a = "and is greater than 5"
b = "and is 0"
c = "and is less than 6 and not 0"


def last_digitor(number):
    if number % 10 == 0:
        return 0
    if number > 0:
        return (number % 10)
    if number < 0:
        return ((number % 10) - 10)


last_digit = last_digitor(number)


if last_digit > 5:
    print("Last digit of {} is {} {}".format(number, last_digit, a))
if last_digit == 0:
    print("Last digit of {} is {} {}".format(number, last_digit, b))
if last_digit < 6 and last_digit != 0:
    print("Last digit of {} is {} {}".format(number, last_digit, c))
