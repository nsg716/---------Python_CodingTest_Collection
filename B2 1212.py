a = input()
b = '0o'+a

c = int(b,8)# 10진수로 변환


result = list(bin(c))

for i in range(len(result)-2):
    print(result[i+2], end ='')
