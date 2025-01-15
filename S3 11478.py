# 서로 다른 부분 문자열의 개수
# 해시를 사용한 집합과 맵

# 방법 1 : 리스트 같이 사용 
# 메모리 : 	238348KB 
# 시간 : 2040ms
S = list(input())
hash = set()
for i in range(len(S)):
    for j in range(0,i+1):
        hash.add(''.join(S[j:i+1]))

print(len(hash))

# 방법 2 : 리스트 없이 사용 
# 메모리 : 	238440KB 
# 시간 : 480ms
S = input() 
hash = set(S[j:i+1] for i in range(len(S)) for j in range(i + 1))

print(len(hash))