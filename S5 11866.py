# 코테 공부 - 알고리즘 유형분석
N, k = map(int, input().split())

x = list(i+1 for i in range(N))
a = 0
y = []

for _ in range(N):
    a += k-1 # 배열의 인덱스 부분이기 때문에 
    a %= len(x) # 배열의 길이가 나누고자하는 수보다 작아지면 안되기에 나머지를 넣는다.
    y.append(x.pop(a))

print(f"<{', '.join(map(str, y))}>")

# 시간 복잡도는 (O(n))