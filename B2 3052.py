# 리스트 생성에 대해서 의문을 가져야 한다.
x = []
for i in range(10):
    inte = int(input())
    if inte%42 not in x:
        x.append(inte%42)

print(len(x))