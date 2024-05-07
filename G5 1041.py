# 그리디 알고리즘 
# 세면이 보이는 부분은 4개 
# 두 면이 보이는 부분은 4 *(2*N-3)개
# 1면이 보이는 부부은 (N-2)(5N-6)개
# 6개 면중 2개의 면을 고르는 수 15개 이중 마주보는 것을 빼면 12개
# 6개 면중 3개의 면을 고르는 수는 20개 이중 마주보는 것을 빼면 17개 
N = int(input())
dice = list(map(int, input().split()))

def get_min3():
    res = 150
    for i in range(4):
        for j in range(i+1, 5):
            if i+ j != 5:
                for k in range(j + 1 , 6):
                    if j+k != 5 and k+i != 5:
                        res = min(res,dice[i]+dice[j]+dice[k])

    return res

def get_min2():
    res = 100
    for i in range(5):
        for j in range(i+1,6):
            if i+j != 5:
                res = min(res,dice[i]+dice[j])

    return res

if N == 1:
    print(sum(dice) - max(dice))
else: 
    print(4*get_min3() + 4 * (2 *N- 3) *get_min2() + (N-2) *(5*N-6) *min(dice)) # 식 