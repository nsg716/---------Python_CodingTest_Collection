# 그리디 알고리즘 

# 최적화 
n = int(input())
count = 0
a = 1000 - n 

coins = [500, 100, 50, 10, 5, 1]

for coin in coins:
    count += a // coin  
    a %= coin           

print(count)

# 명시적 반복문 
n = int(input())
count = 0
a = 1000 - n 

while a>=500:
 
    count += 1
    a -= 500

while a>=100:
     
    count += 1
    a -= 100
    
while a>=50:
     
    count += 1
    a -= 50
    
while a>=10:
     
    count += 1
    a -= 10

while a>=5:
     
    count += 1
    a -= 5

while a>=1:
     
    count += 1
    a -= 1
    
print(count)




