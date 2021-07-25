'''
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
'''

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    number = int(raw_input().strip())
    
    if number % 2 != 0:
        print("Weird")
    if number % 2 == 0 and number >= 2 and number <= 5:
        print("Not Weird")
    if number % 2 == 0 and number >= 6 and number <= 20:
        print("Weird")
    if number % 2 == 0 and number > 20:
        print("Not Weird")
