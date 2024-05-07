# 완전탐색의 경우는  복잡도가 O(N^3)이다. 
# 동적 계획법으로 풀수 밖에 업다. 

# 점화식 DP (i,j) = min(DP(i-1,j-1),DP(i-1,j),DP(i,j-1)) +1
# 점화식으로 만든 값의 정체는  가장 큰 정사각형의 한변의 길이이다.  따라서 구한 값을 제곱을 하면 된다. 

n,m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
ans = max(arr[0])
for i in range(1,n):
    for j in range(1,m):
        if arr[i][j] == 1:
            arr[i][j] = min(arr[i-1][j-1], arr[i-1][j], arr[i][j-1] ) + 1

    ans = max(ans,max(arr[i]))

print(ans ** 2)