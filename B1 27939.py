# 구현 
import sys
imput = sys.stdin.readline

n = int(input())
kind = list(input().rstrip().split())
m , k = map(int, input().split())
assist = []


for _ in range(m):
    assist.append(list(map(int,input().split())))
    
    
# 입력한 배열과 주어진 배열에서 모두 W 로 이루어졌으면 W출력 
# 그렇지 않으면 P를 출력 
# 문제를 어렵게 작성해서 그렇지 P만 없으면 W출력 그렇지 않으면 P를 출력하면 된다.
for i in assist:
    for j in i:
        if kind[j-1] == "P":
            break
    else:  
        print("W")
        break
else:
    print("P")