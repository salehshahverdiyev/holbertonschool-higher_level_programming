#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


number = str(number)
a = "and is greater than 5"
b = "and is 0"
c = "and is less than 6 and not 0"


def last_digitor(number):
    if int(number[-1]) == 0:
        return 0
    if int(number) > 0:
        return (int(number[-1]))
    if int(number) < 0:
        return (int(number[-1]) * -1)


last_digit = last_digitor(number)


if last_digit > 5:
    print("Last digit of {} is {} {}".format(number, last_digit, a))
if last_digit == 0:
    print("Last digit of {} is {} {}".format(number, last_digit, b))
if last_digit < 6 and last_digit != 0:
    print("Last digit of {} is {} {}".format(number, last_digit, c))
