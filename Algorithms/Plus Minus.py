# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with  places after the decimal.
# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, 
# though answers with absolute error of up to  are acceptable.

# Example
# arr = [1,1,0,-1,-1]
# There are  elements, two positive, two negative and one zero. Their ratios are 2/5 = 0.400000, 2/5 = 0.400000 and 1/5 = 0.200000. 
# Results are printed as:
# 0.400000
# 0.400000
# 0.200000

## Function Description
# Complete the plusMinus function in the editor below.
# plusMinus has the following parameter(s):
# int arr[n]: an array of integers

## Print
# Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. 
# The function should not return a value.

### SOLUTION
#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    pos = 0
    neg = 0
    z = 0
    for i in range(0, len(arr)):
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
        else:
            z += 1
    print(pos / len(arr))
    print(neg / len(arr))
    print(z / len(arr))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)