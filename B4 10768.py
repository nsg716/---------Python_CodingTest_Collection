N1 = int(input())
N2 = int(input())
if (N1 == 2):
    if (N2 == 18):
        print("Special")
    elif N2 < 18:
        print("Before")
    else :
        print("After") 
elif (N1 > 2):
    print("After")
elif (N1 < 2):
    print("Before") 