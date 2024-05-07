# 스택 수열 
# 입력한 수를 스택을 통해 수열을 만들 수 있는가를 묻는 문제다.

flag = True
count = 1
x = []
opration = []
N = int(input())

for i in range(N):
    number = int(input())
 
    while count <= number:
        x.append(count)
        opration.append('+')
        count+=1
     
     
    if x[-1] == number: 
        x.pop()
        opration.append('-')
    else:
        flag = False
        break
    
if flag == False:
    print("NO")
else:
    for i in opration:
        print(i)