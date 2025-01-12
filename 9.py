N = int(input())
x  = []
for i in range(N-1):
    a,b = map(int,input().split())
    x.append([a,b])

for i in range(len(x)):
    for j in range(len(x)):
       if x[i][0] == x[] 


## 리스트 안에 중복 문자열을 처리하지 못해서 문제가 발생
"""
result = 0
key = 0
count = 1
while count:
       if key == 0:
              for i in range(len(x)):
                     if 1 == x[i][0]:
                            key = x[i][1]
                            result += x[i][1]
                     
       elif key != 0 :
              for i in range(len(x)):
                     if key == x[i][0]:
                            key = x[i][1]
                            result += x[i][1]
                     else:
                            count = 0
print(result)
"""
