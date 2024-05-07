import math

N1 = int(input())
N2 = int(input())
pow1 = list(0 for i in range(int(math.sqrt(N2)+1)))

while 1 :
    try:
        sum = 0
        min = 0
        for i in range(1,int(math.sqrt(N2)+1)):
            pow1[i] = i*i
        
            if N1 <= pow1[i] and N2 >= pow1[i]:
                sum += pow1[i]
            print(sum)
            print(min(pow1))
    except:
        print("-1")
        break