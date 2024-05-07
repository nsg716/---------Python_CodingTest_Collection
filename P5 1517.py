#doit 파이썬 코테 준비 : 021번
# 버블 정렬 swap이 일어난 횟수 구하기 버불 정렬 쓰면 시간 초과가 일어난다. 따라서 O(nlogn)을 써야 한다.
# 병합 정렬을 이용한다. 

import sys 
input = sys.stdin.readline
result = 0

def merge_sort(s,e):
    global result
    if e - s < 1: return 
    m = int(s+ (e-s) / 2)
    # 구간 나누기
    merge_sort(s,m)
    merge_sort(m+1,e)
    
    for i in range(s,e+1):
        tmp[i] = A[i]
    k =  s
    index1 = s
    index2 = m + 1
    
    while index1 <= m and index2 <= e: # 두 그룹을 병합하는 조직
        if tmp[index1]> tmp [index2]:
            A[k] = tmp[index2]
            result = result + index2 -k #뒤쪽 데이터 값이 더 작다면 데이터 업데이트 
            k += 1
            index2 += 1
        else :
            A[k] = tmp[index1]
            k+= 1
            index1 += 1
    while index1 <= m:
        A[k] = tmp[index1]
        k+= 1
        index1 += 1
        
    while index2 <= e:
        A[k] = tmp[index2]
        k+= 1
        index2 += 1
        
N = int(input())
A = list(map(int, input().split()))
A.insert(0,0)

tmp = [0] * int(N + 1)
merge_sort(1,N)
print(result)  