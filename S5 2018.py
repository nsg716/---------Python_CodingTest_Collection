#doit 파이썬 코테 준비 : 006번
# 투 포인터 문제로 시간복잡도를 O(nlogn)에서 O(n)으로 낮출 수 있는 기법중 하나이다.
n = int(input())

# 자기 자신을 포함 
count = 1
start_index  = 1
end_index  = 1

sum = 1

while end_index != n:
    if sum == n: 
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
        
    else:
        end_index += 1
        sum += end_index
print(count)