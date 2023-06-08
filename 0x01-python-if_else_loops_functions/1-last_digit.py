#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if digit > 5:
    evaluation = "and is greater than 5"
elif digit == 0:
    evaluation = "and is 0"
else:
    evaluation = "and is less than 6 and not 0"

print(f"Last digit of {number} is {digit} {evaluation}")
