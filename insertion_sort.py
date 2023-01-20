#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#


def insertionSort1(n, arr):
    # Write your code here
    target = arr[-1]
    i = n-2
    while target < arr[i] and i >= 0:
        arr[i+1] = arr[i]
        i -= 1
        print(*arr)
    arr[i+1] = target
    print(*arr)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
