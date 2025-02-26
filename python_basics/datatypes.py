#!/usr/bin/env python3
""" This module contains a function convert """


def convert():
    """ Converts integer variable to float and vice versa
        Prints the type of each variable declared """
    # Initialize the variables
    a = 2
    b = 2.5
    c = 4 + 2j
    d = [3, 4]
    e = (2, 4)
    f = {"name": "Jude", "level": "38"}
    g = {"bob", "chandler"}
    h = True

    # Print the types of the variables
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))
    print(type(f))
    print(type(g))
    print(type(h))

    x = 3  # Initialize int 3
    float_x = float(x)  # Convert to float
    print(float_x)
    x = int(float_x)  # Change the float back to int
    print(x)


convert()
