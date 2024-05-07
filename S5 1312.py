# 손으로 나누기 하는 과정을 코딩으로 만듬

a, b, c = map(int,input().split())

a%=b

for i in range(c-1):
    a = (a*10) % b
    
res = (a*10 )//b
print(res)

