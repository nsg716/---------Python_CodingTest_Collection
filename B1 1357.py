a, b = map(str, input().split())
a= a[::-1]
b = b[::-1]
a = int(a)
b = int(b)
res = a+b
res = str(res)
res = res[::-1]
res = int(res)
print(res)