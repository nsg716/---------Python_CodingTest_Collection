
a = input()

res = 0

for i in range(1,len(a)):
    res += 9 * (10 ** (i-1)) * i # 자리수 
    
res += (int(a) - (10 ** (len(a)-1)) + 1) * len(a)

print(res)

