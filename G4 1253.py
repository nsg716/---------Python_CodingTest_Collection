#doit 파이썬 코테 준비 : 008번

import sys
input = sys.stdin.readline 
N = int(input())
result = 0
A = list(map(int, input().split()))
A.sort()

for k in range(N):
    find = A[k]
    i = 0
    j = N - 1
    while i < j: 
        if A[i] + A[j] == find : 
            if i != k and j != k:
                result += 1
                break
            elif i == k:
                i+=1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < find:
            i+= 1 # start index + 1 을 한다. 
        else: # A[i] + A[j] > find 인경우 
            j-=1
print(result)
