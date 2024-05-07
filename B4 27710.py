N = int (input())
a, b, c = map(int,input().split())
sum = 0
if (a>= N):
    sum += N
elif (a <N ):
    sum +=a 

if (b>= N):
    sum += N
elif (b <N ):
    sum +=b  

if (c>= N):
    sum += N
elif (c <N ):
    sum +=c 

print(sum)