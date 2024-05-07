# 절사평균
# round 함수의 특성 파악하기 특히 오사오입인데  사사오입이라고 잘 못 쓰지 않기 
import sys

def roundUp(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

N = int(sys.stdin.readline())
x = []
if N== 0:
    print(0)
else:
    
    for i in range(N):
        x.append(int(sys.stdin.readline()))
    
    x.sort()
    length = len(x)  
    average = roundUp(length*0.15)

 
    x = x[average:N-average]
    print(roundUp(sum(x)/len(x))) 