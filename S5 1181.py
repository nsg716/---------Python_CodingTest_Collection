import sys
N = int(sys.stdin.readline())
x = []
y = []

for i in range(N):
    x.append(sys.stdin.readline().strip())

y = list(set(x))
y.sort()
y.sort(key=len)

for i in y:
    print(i)

"""
for i in range(N):
    for j in range(N):
        if len(x[i]) < len(x[j]):
            asca = x[j]
            x[j] = x[i]
            x[i] = asca
for i in range(N-1):
    if len(x[i]) == len(x[i+1]):
        if x[i] > x[i+1]:
            asca = x[i]
            x[i] = x[i+1]
            x[i+1] = x[i] 
"""

