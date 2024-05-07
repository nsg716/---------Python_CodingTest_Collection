
#시간날때 다시풀기
import sys
from collections import Counter

N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
y = list(map(int, sys.stdin.readline().split()))

c = Counter(x)

print(' '.join (f'{c[i]}'if i in c else '0' for i in y))
