# Given an array of integers, find the sum of its elements.
# For example, if the array ar = [1,2,3],1+2+3 =6, so return 6.

# Function Description

# Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.
# simpleArraySum has the following parameter(s)
# ar: an array of integers


#!/bin/python3

import math
import os
import random
import re
import sys


def simpleArraySum(ar):
    result = 0
    for i in range(0,ar_count):
        result = result + ar[i]
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()