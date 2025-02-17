# Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, 
# determine the number of apples and oranges that land on Sam's house.

# In the diagram below:

# The red region denotes the house, where  is the start point, and  is the endpoint. The apple tree is to the left of the house, and the orange tree is to its right.
# Assume the trees are located on a single point, where the apple tree is at point , and the orange tree is at point .
# When a fruit falls from its tree, it lands  units of distance from its tree of origin along the -axis. *A negative value of  means the fruit fell  
# units to the tree's left, and a positive value of  means it falls  units to the tree's right. *

# Given the value of  for  apples and  oranges, determine how many apples and oranges will fall on Sam's 
# house (i.e., in the inclusive range )?

# For example, Sam's house is between  and . The apple tree is located at  and the orange at . 
# There are  apples and  oranges. Apples are thrown  units distance from , and  units distance. 
# Adding each apple distance to the position of the tree, they land at . Oranges land at . 
# One apple and two oranges land in the inclusive range  so we print

#SOLUTION
#!/bin/python3

import math
import os
import random
import re
import sys


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    orange_count = 0
    for i in range(len(apples)):
        if a + apples[i] >= s and a + apples[i] <= t:
            apple_count += 1
    for j in range(len(oranges)):
        if b + oranges[j] >= s and b + oranges[j] <= t:
            orange_count += 1
    return apple_count, orange_count

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    apple_count, orange_count = countApplesAndOranges(s, t, a, b, apples, oranges)
    print(apple_count)
    print(orange_count)