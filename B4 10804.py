x = [i+1 for i in range(20)]

for i in range(10):
    a, b = map(int, input().split())
    a -= 1
    x[a:b] = x[a:b][::-1]
    
print(*x) # 리스트 언패킹 [1,2,3]을 1,2,3으로 출력해줌. 이걸 왜 이제야...


"""
for i in range(int(b-a//2)):
    temp = x[20-b-i] 
    x[20-b-i] = x[a+i]
    x[a+i] = temp 
    print(x)
    """