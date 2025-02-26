#!/usr/bin/env python3
""" This module contains numpy basic operations """

import numpy as np

# Creating an array
a = np.array([1, 2, 3, 4, 5, 6])
print(a)

# Print the first element of the array
print(a[0])

# Slicing to obtain the first 3 elements of the array
print(a[:3])

# Changing the first element of the array
a[0] = 20
print(a)

# Creating a multidimensinal array
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(b)
