#!/usr/bin/env python3
""" This module contains funtion calculate_area """

import math


def calculate_area(shape, dimension1, dimension2=0):
    """ Calculates and returns the area of a given shape """
    if shape == "circle":
        return math.pi * (dimension1 ** 2)
    elif shape == "rectangle":
        return dimension1 * dimension2
    elif shape == "triangle":
        return 0.5 * dimension1 * dimension2


t1 = ("triangle", 2, 3)  # Create a tuple object which represents a triangle
print(calculate_area(*t1))  # Unpack the tuple into the function

c1 = ("circle", 3)
print(calculate_area(*c1))

r1 = ("rectangle", 4, 5)
print(calculate_area(*r1))

c2 = ("circle", 12)
print(calculate_area(*c2))
