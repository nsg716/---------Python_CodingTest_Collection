cook = int(input())
A = 0
B= 0
C = 0
if (cook % 10 != 0):
    print("-1")
else :
    A = cook // 300 
    B = ((cook % 300) // 60 )
    C = (((cook % 300) % 60 ) // 10)
    print(A, B, C)