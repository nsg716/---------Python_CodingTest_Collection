N = int(input())
arr = list(map(int, input().split()))

count = 0
for i in range(len(arr)):
    if arr[i] == N:
        count += 1

print(count)