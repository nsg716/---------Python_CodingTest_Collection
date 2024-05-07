n, k= map(int, input().split())

str_len = 1 # 숫자 길이
str_num = 9 # 길이에 따른 숫자의 개수 1:9, 2:90, 3:900...
check = 0

while (k > str_len*str_num):
    k-=str_len*str_num
    a = k
    check += str_num
    str_len +=1 
    str_num*=10


Ind= int((k-1) % str_len) # 문자열 자리
res = int((check+1+((k-1)/str_len)))

if (res>n):
    print("-1")
else:
    res = str(res)
    print(res[Ind])
