#!/usr/bin/env python3
""" This module contains a functions check_even and even_or_odd """


def check_even():
    """ Checks if a user inputted number is even or odd
        Return: True is the integer is even, else False """
    user_int = int(input("Enter an integer: "))
    if (even_or_odd(user_int)):
        print("The number is even")
    else:
        print("The number is odd")

    print("Numbers from 0 to 50: ")
    i = 0
    for i in range(0, 51):
        if even_or_odd(i):
            print(i)

    print("Numbers counted down from 10 to 1: ")
    j = 10
    while (j > 0):
        print(j)
        j -= 1


def even_or_odd(k):
    """ Checks if a number is even or odd
        Return: True if the number is even, else False """
    if k % 2 == 0:
        return True
    else:
        return False


check_even()
