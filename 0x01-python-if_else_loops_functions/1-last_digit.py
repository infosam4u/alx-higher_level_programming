#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
if number[-1] > '5':
    if number < '0':
        print(f"Last digit of {number} is -{number[-1]} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {number[-1]} and is greater than 5")
elif number[-1] == '0':
    if number < '0':
        print(f"Last digit of {number} is -{number[-1]} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {number[-1]} and is zero")
else:
    if number < '0':
        print(f"Last digit of {number} is -{number[-1]} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {number[-1]} and is less than 6 and not 0")
