"""
    Tasks:
    The provided code stub reads and integer, n , from STDIN. For all non-negative integers i<n^2  print i^2 .
"""

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)