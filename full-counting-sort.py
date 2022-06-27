#!/bin/python3

import math
import os
from pickletools import stringnl
import random
import re
import sys
import collections
#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    result = [[] for i in range(100)]
    n = len (arr)
    for i in range(n//2):
        result[int(arr[i][0])].append('-')
    
    for i in range(n//2, n):
        result[int(arr[i][0])].append(arr[i][1])
    
    for string in result:
        if string:
            print(*string,end=" ")



if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
