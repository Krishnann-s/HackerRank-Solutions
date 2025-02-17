# You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a 
# number line ready to jump in the positive direction (i.e, toward positive infinity).

# The first kangaroo starts at location  and moves at a rate of  meters per jump.
# The second kangaroo starts at location  and moves at a rate of  meters per jump.
# You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. 
# If it is possible, return YES, otherwise return NO.

#SOLUTION
#!/bin/python3

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    if x2>x1 and v2>v1:
        return "NO"
    elif v2!=v1 and (x2-x1) % (v2-v1) == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
