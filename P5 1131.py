#  동적계획법으로 푼다. 수열이지만 사이클이 생긴다. 이 사이클 중에서 가장 작은값이면서 사이클이 발생하는 수를 찾으면 된다. 
# 메모이제이션 : 값비싼 함수 호출의 결과를 캐싱하고 동일한 입력이 다시 발생할 때 불필요하게 다시 계산하는 대신 캐싱된 결과를 반환하는 프로그래밍 기술
# 이를 이용하여 시간 복잡도를 줄인다. 

INF = 9876543210
cache = [INF] * 10_000_001 # 초기값 : INF, 임시마크 : 0
A,B,K = map(int, input().split())

def S(n):
    return sum(int(ch) ** K for ch in str(n))

def dfs(n):
    if cache[n] == INF: # 최초 방문 노드
        cache[n] = 0 # 임시마크 등록 이후 탐색 시작
        cache[n] = min(n,dfs(S(n)))
    else :
        # 이미 탐색 완료한 노드라면 바로 반환 
        if cache[n]:
            return cache[n]
        
        # 탐색중인 노드 재방문, 즉 사이클 발견 -> 최솟값을 찾는다.
        m = n 
        nn =S(n)
        while nn != n:
            m = min(m,nn)
            nn = S(nn)

        # 사이클에서 최솟값 갱신
        cache[n] = m
        nn= S(n)
        while nn != n:
            cache[nn] = m
            nn = S(nn)

    return cache[n]

print(sum(dfs(i) for i in range(A,B+1)))