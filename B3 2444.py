# 별찍기
N = int(input())
NN = 2*N-1
lang = "*"
for i in range(1,N):
    print(" " * (N-i)  + "*" * (2*i-1) )
for i in range(N,0,-1):
    print(" " * (N-i)   + "*" * (2*i-1))