# 모등 경우의 수는 25200이며, (a+b+c+d)! / a!*b!*c!*d! 이며 모든 가능한 식을 만들어 보고 이를 최댓값과 최솟값을 찾는 방법으로 푼다. 
# 아래의 경우는 순열을 통해 풀었으며, 중복이 많이 발생하기에 집합을 통해 문제를 해결한다.

from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
ops_cnt = []
for i,cnt in enumerate(map(int, input().split())):
    ops_cnt += [i] * cnt
    
ans_max = -1_000_000_001
ans_min = 1_000_000_001

for permu in set(permutations(ops_cnt,N-1)):
    res = nums[0]
    for i,op in enumerate(permu):
        if op == 0:
            res += nums[i+1]
        elif op ==1:
            res -= nums[i+1]
        elif op == 2:
            res *= nums[i+1]
        else:
            if res >= 0:
                res //=nums [i+1]
            else:
                res = -(-res//nums[i+1])


    if res > ans_max:
        ans_max = res
    
    if res < ans_min:
        ans_min = res

print(ans_max)
print(ans_min)