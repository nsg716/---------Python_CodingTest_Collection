a, b =map(int,input().split())
c = int(input())
n = int(input())
if (((a-c)*n+b) <= 0) and a<=c :
    print(1)
else :
    print(0)