import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque(enumerate(map(int, sys.stdin.readline().split()))) #1
res = []

while q:
    idx, num = q.popleft() #2
    res.append(idx+1) #3
    if num > 0: #4
        q.rotate(-1*(num-1))
    elif num < 0: #5
        q.rotate(abs(num))
print(*res)