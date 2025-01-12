s = list(input())
result = 0
count = 0
ma = 0

for i in s:
    if i == "(":
        ma += 1
        count = 0
    elif i == ")":
        ma -=1
        
        if count == 0:
            result += ma
            count = 1
        else:  
            result += 1

print(result)

## 재미 있었다.