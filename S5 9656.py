N = int(input())
count = 0
while N >= 0:
    if N%3 == 0:
        count += N//3    
        break
    N -= 1
    count+= 1
if count % 2== 1:
   print("CY")
else :
    print("SK")
