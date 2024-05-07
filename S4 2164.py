N = int(input())

bin = 2
while 1:
    if (N == 1 or N== 2):
        print(N)
        break
    bin *= 2
    if  bin >= N:
        print((N - (bin // 2)) * 2)    
        break