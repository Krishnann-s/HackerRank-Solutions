#!/bin/python3

import math
import os
import random
import re
import sys


def migratoryBirds(arr):
    d = {1:0, 2:0, 3:0, 4:0, 5:0}
    for i in arr:
        if i in d:
            d[i] += 1
    max_count = max(d.values())
    most_common_bird = min(key for key, value in d.items() if value == max_count)
    return most_common_bird
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
