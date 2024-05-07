# 1은 2초, 2이상부터 1초씩 증가함.
phone = ['ABC', 'DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
AA = input()
sum = 0
for i in range(len(AA)) : 
    for j in phone :
        if  (AA[i] in j) :
            sum += phone.index(j)+ 3
print(sum)