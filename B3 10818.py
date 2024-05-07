# 리스트의 최솟값 최댓값 출력
n = int(input())
n_list = list(map(int, input().split()))
min = 1000000
max = -1000000
for i in range(len(n_list)):
    if min > n_list[i]:
        min = n_list[i] 
    if max < n_list[i]:
        max = n_list[i]
print(min, max)