A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
result = B-A
sum1 = 0
if A < 0 : 
    sum1 += C*abs(A) + D
    sum1 += E*B 
    print(sum1)

else:
    sum1 += E * result
    print(sum1)