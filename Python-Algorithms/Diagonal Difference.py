# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
## For example, the square matrix  is shown below:
# 1 2 3
# 4 5 6
# 9 8 9  
# The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

## Function description
# Complete the  function in the editor below.
## diagonalDifference takes the following parameter:
# int arr[n][m]: an array of integers

## Return
# int: the absolute diagonal difference

## Input Format
# The first line contains a single integer, , the number of rows and columns in the square matrix .
# Each of the next  lines describes a row, , and consists of  space-separated integers .

## Constraints
# -100 <= ar[i][j] <=100

## Output Format
# Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

## Sample Input
# 3
# 11 2 4
# 4 5 6
# 10 8 -12

## Sample Output
# 15

### SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    d1, d2 = 0, 0
    for i in range(0, len(arr)):
        d1 += arr[i][i]
    for j in range(0, len(arr)):
        d2 += arr[j][len(arr) - 1 - j]
    return abs(d1 - d2)
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()