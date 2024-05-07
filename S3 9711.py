import sys
con = int(sys.stdin.readline())
x = [1,1]

for i in range(10000):
    x.append(x[i] + x[i+1])
x.pop()
x.pop()



j = 1
for _ in range(con):
    N, M = map(int, sys.stdin.readline().split())
    

    res = x[N-1]%M
    print("Case #%d: %d" %(j,res))
    j+= 1
