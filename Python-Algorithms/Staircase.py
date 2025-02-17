# Staircase detail
# This is a staircase of size :

#    #
#   ##
#  ###
# ####
# Its base and height are both equal to . It is drawn using '#' symbols and spaces. The last line is not preceded by any spaces.
# Write a program that prints a staircase of size .

## Function Description
# Complete the staircase function in the editor below.
# staircase has the following parameter(s):
# int n: an integer
# Print
# Print a staircase as described above.

# SOLUTION
#!/bin/python3

import math
import os
import random
import re
import sys


def staircase(n):
    k = n - 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("#", end="")
        print("\r")

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)