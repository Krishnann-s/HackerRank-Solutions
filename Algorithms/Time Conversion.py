# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Example
# s ='12:01:00PM'
# Return '12:01:00'.

#s ='12:01:00AM'
# Return '00:01:00'.

## Function Description
# Complete the timeConversion function in the editor below. It should return a new string representing the input time 
# in 24 hour format.
# timeConversion has the following parameter(s):
# string s: a time in  hour format

## Returns
# string: the time in 24 hour format

# Input Format
# A single string  that represents a time in -hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM).

## Constraints
# All input times are valid

## SOLUTION
#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    t = s.split(':')
    if t[-2:] == 'PM':
        if t[0] != '12':
            t[0] = str(int(t[0])+12)
    else:
        if t[0] == '12':
            t[0] == '00'
    time = ':'.join(t)
    return str(time[:-2])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()