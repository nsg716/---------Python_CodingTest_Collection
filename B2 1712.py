a, b, c = map(int, input().split())
money = c-b
if money <=0 :
    print("-1") 
else :
    result =  a // money
    print(result+1)