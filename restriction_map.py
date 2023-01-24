import re
import Bio
import numpy as np
from turtle import *
# Given: A multiset L containing (n2)
# positive integers for some positive integer n

# Obtain L corresponding to the distances between restriction sites on chromosome

# Return: A set X containing "n" non-negative integers such that
# ΔX = L

x = np.array([2, 2, 3, 3, 4, 5, 6, 7, 8, 10])

# L = [0, 2, 3, 7, 10]
x = np.unique(x)
print (x)
distance = []
for i in x:
    distance.append((i+3) - i)

print (distance)






