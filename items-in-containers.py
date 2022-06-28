#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numberOfItems' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY startIndices
#  3. INTEGER_ARRAY endIndices
#

def numberOfItems(s, startIndices, endIndices):
    # Write your code here
    ln = len(s)
    # pre-calc left-most pipe location and sum of stars arrays
    stars = [0] * (ln+1)
    lftpipeidx = [-1] * (ln+1)
    for i, ch in enumerate(s,1):
        if ch == "|":
            stars[i] = stars[i-1]
            lftpipeidx[i] = i
        else:  # ch == *
            stars[i] = stars[i-1] + 1
            lftpipeidx[i] = lftpipeidx[i-1]
    if lftpipeidx[-1] == -1:
        return [0]*len(startIndices)

    # pre-calc right-most pipe location
    rgtpipeidx = [ln+1] * (ln+1)
    for i in range(ln-1,-1,-1):
        if s[i] == '|':
            rgtpipeidx[i+1] = i+1
        else:
            rgtpipeidx[i+1] = rgtpipeidx[i+2] if i < ln-1 else ln+1

    # calc answer as difference between num. of stars b/w right and left pipes.
    # right pipe is the left-most pipe from the end index, left pipe is the right-most one from the start index
    ans = []
    for i in range(len(startIndices)):
        si, ei = startIndices[i], endIndices[i]
        lftpipe = rgtpipeidx[si]
        rgtpipe = lftpipeidx[ei]
        ans.append(stars[rgtpipe] - stars[lftpipe] if lftpipe < rgtpipe else 0)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    startIndices_count = int(input().strip())

    startIndices = []

    for _ in range(startIndices_count):
        startIndices_item = int(input().strip())
        startIndices.append(startIndices_item)

    endIndices_count = int(input().strip())

    endIndices = []

    for _ in range(endIndices_count):
        endIndices_item = int(input().strip())
        endIndices.append(endIndices_item)

    result = numberOfItems(s, startIndices, endIndices)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
