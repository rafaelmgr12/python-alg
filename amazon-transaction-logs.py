#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER threshold
#

def processLogs(logs, threshold):
    print(logs,threshold)
    # Write your code here
    user_map = {}
    for log in logs:
        log_arr = log.split(" ")
        user_map[log_arr[0]] = user_map.get(log_arr[0], 0) + 1
        if (log_arr[0] != log_arr[1]):
            user_map[log_arr[1]] = user_map.get(log_arr[1], 0) + 1
    target_users = []
    for key, val in user_map.items():
        if (val >= threshold):
            target_users.append(key)
    print(target_users)
    return target_users
        

        
        
            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    threshold = int(input().strip())

    result = processLogs(logs, threshold)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
