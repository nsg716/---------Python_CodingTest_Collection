# 스택으로 구현 
import sys
input = sys.stdin.readline

N,P = map(int, input().split())
ans = 0 
stk = [[] for _ in range(7)]
for _ in range(N):
    line, p = map(int,input().split())
    while stk[line] and stk[line][-1] > p:
        stk[line].pop()
        ans+=1
    # 이미 스택안에 있으면 ==> 누르고 있으면 
    if stk[line] and stk[line][-1] == p:
        continue

    stk[line].append(p)
    ans+=1
print(ans)