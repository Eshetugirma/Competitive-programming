#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
def arrayManipulation(n, queries):
    # Write your code here
    arr = [0]*n
    for left,right,val in queries:
        arr[left-1] += val
        if right < n:
           arr[right] -= val
    prf = [0]
    for i in arr:
        prf.append(prf[-1]+i)
    return max(prf)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    
    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
