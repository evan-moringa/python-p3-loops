#!/usr/bin/env python3

def happy_new_year():
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")

def square_integers(nums):
    squared_nums = [num ** 2 for num in nums if isinstance(num, int)]
    return squared_nums


def fizzbuzz():
    for num in range(1, 101):
        output = ""
        if num % 3 == 0:
            output += "Fizz"
        if num % 5 == 0:
            output += "Buzz"

        if output == "":
            output = num

        print(output)



