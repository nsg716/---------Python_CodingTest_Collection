import sys
import math

a, b, c = map(int, sys.stdin.readline().split())
day = (c - b) / (a -b)
print(math.ceil(day))