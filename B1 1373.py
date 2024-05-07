a = input()
b = '0b'+a

c = int(b,2)# 10진수로 변환
result = list(oct(c))

for i in range(len(result)-2):
    print(result[i+2], end ='')