#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
def last_digitor(number):
    if int(number[-1]) == 0:
        return 0
    if int(number) > 0:
        return (int(number[-1]))
    if int(number) < 0:
        return (int(number[-1]) * -1)
last_digit = last_digitor(number)
if last_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_digit))
if last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit))
if last_digit < 6 and last_digit != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_digit))
