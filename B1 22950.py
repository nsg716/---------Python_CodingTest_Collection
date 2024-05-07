N = int(input())
N1 = input()
N2 = int(input())
N1 = "0b"+N1
N1 = int(N1,2)
if N1 % 2**N2 == 0:
    print("YES")
else : 
    print("NO")
