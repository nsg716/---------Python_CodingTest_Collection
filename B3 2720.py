N = int(input())
for i in range(N):
    a = int(input())
    a1 = a//25
    a2 = (a%25)//10
    a3 = ((a%25)%10)//5
    a4 = (((a%25)%10)%5)

    print(a1,a2,a3,a4)