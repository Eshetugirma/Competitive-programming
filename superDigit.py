#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n 
#  2. INTEGER k 
#

def superDigit(n, k):
    # Write your code here
    p = 0
    string = str(n)
    for i in string:
        p += int(i)
    p *= k
    start = str(p)
    def superity(p,temp):
        if int(p) <= 9:
            return int(p)
        for i in p:
            temp += int(i)
        p = str(temp)
        
        return superity(p,0)
    return superity(start,0)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
