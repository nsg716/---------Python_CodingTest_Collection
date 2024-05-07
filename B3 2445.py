
# 별찍기
N = int(input())
for i in range(N):
    lang = "*"
    print(lang*(i+1) + " " * (2*(N-i-1)) + lang*(i+1))
for i in range(1,N):
    print(lang*(N-i) +" " * (2*(i)) + lang*(N-i))


