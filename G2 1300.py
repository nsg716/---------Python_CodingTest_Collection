# doit 파이썬 코테 준비 : 031번
# 2차원 배열을 1차원 배열로 만들어지고, 배열의 크기와 인덱스가 주어졌을 때, 그 값을 찾는 법 
# 이진 탐색으로 풀어야 한다. O(N^2)을 고민해야한다. 
import sys
input = sys.stdin.readline
N = int(input())
K = int(input())

start = 1
end = K
ans = 0

while start <= end:
    middle = int((start + end) / 2)
    cnt = 0
    for i in range(1,N+1):
        cnt += min(int(middle / i), N)
    if cnt < K:
        start = middle + 1
    else: 
        ans = middle
        end = middle - 1
        
print(ans)