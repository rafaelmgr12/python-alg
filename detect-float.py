"""You are given a string N.
Your task is to verify that N is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == "__main__":
    t = int(input().strip())
    pattern = '^[+-]?[0-9]*\.[0-9]+$'
    
    for _ in range(t):
        print(bool(re.match(pattern, input())))