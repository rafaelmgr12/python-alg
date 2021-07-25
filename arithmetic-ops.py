"""Task
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
"""
import sys


def constraints(a):
    if a >= 1 and a <= 10**10:
        return True
    else:
        return False


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    if not(constraints(a) and constraints(b)):
        print("It's not in the interval of 1< a < 10^10")
        sys.exit()

    print(a + b)
    print(a-b)
    print(a*b)
