# 대표적인 백트레킹 문제 완전탐색의 경우 O(2^N^2)의 시간 복잡도를 가진다. 
# 행마다 퀸을 두면 행마다 퀸이 있는지 없는지 확인하는 재귀함수를 만든다. 
# 하지만 다음과 같은 방법이면 시간복잡도는 O(N)이 되어서 시간초과가 일어난다.
# 열마다 퀸이 있는지 없는디 체크하는 체크배열을 전역변수에 놓는다. 퀸을 둔 열의 인덱스를 체크한다. 


# 범위가 1~14이므로 정답의 정수 역시 1개로 고정이 된다. 테스트 케이스는 14가지이다. 14가지의 정답을 적는 방법 - 좋지 않은 해결방법
# 퀸을 전부 완성한 모습에서 좌우로 뒤집는 방법도 1개의 방법이다. 하나의 경우를 구하면 2개의 가지수가 나온다.
# 다만 N이 홀수이면 그에 따른 케이스도 생각을 해야하므로 이 경우를 따로 제외한다. 
N = int(input())
ans = 0
col = [False] * N # i 번째에 퀸을 두었다. 
d1 = [False] * 2 * N # \ 대각선, 우상단부터 0
d2 = [False] * 2 * N # / 대각선, 좌상단부터 0

# Backtracking
def backtracking (row):
    global ans
    if row  == N:
        ans += 1
        return 
    
    for j in range(N if row else N // 2):
        if not col[j] and not d1[row-j] and  not d2[row+j]:
            col[j] = True
            d1[row-j] = True
            d2[row+j] = True

            backtracking(row+1)

            # 원상복구
            d2[row+j]= False
            d1[row-j] = False
            col[j] = False


if N%2:# 홀수일때,
    backtracking(0)
    ans*=2

    # 정가운데 퀸이 있는 경우의 수를 더한다. 
    j  = N //2 
    col[j] = d1[-j] = d2[j] = True
    backtracking(1)

    print(ans)
else :
    # 짝수일 때는 절만만 두고 그 경우의 수룰 2배한다. 
    backtracking(0)
    print(ans*2)