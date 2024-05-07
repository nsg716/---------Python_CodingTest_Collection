a, b = input().split()
a = "0b"+a
b = "0b"+b
res = int(a,2)+int(b,2)
res = bin(res)
print(res[2:])