# doit 파이썬 코테 준비 : 097번 
# 기하 알고리즘을 다룰 때 이용하는 CCW라는 기술을 사용 -  평면상의 3개의 점과 관련된 점들의 위치관계를 판단하는 알고리즘 


import sys 
input = sys.stdin.readline
x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
x3,y3 = map(int, input().split())

#CCW 공식 
result = (x1*y2 + x2 * y3 + x3*y1) - (x2*y1 + x3*y2 + x1* y3) 

if result > 0 :
    print(1)
elif result < 0:
    print(-1)
else:
    print(0)