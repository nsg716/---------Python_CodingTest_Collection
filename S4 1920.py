import sys

N = int(sys.stdin.readline())

x = set(map(int, sys.stdin.readline().split()))# 리스트로 하면 중첩된 것 까지 찾아야 하니 시간이 많이 든다.

M = int(sys.stdin.readline())

y = list(map(int, sys.stdin.readline().split())) 

for i in y:
    if i in x: # y 리스트 중에 x 가 있으면 이라는 조건문
        print("1")
    else : 
        print("0")