N = int(input())
for i in range(0,N-1):
    if i == 0:
        a=0
    else :
        a = 1
    print(" " * (N-i-1) + "*" + " " * (2*i-1) + "*" *a )
for i in range(N-1,N):
    print("*"* (2*i+1))