# 프로그래머스 검색을 할때에는 이름으로 검색을 해야 결과를 얻을 수 있다. 
# 문제 1번 : 다트 게임 
# 구현력을 요구하는 문제에 대해서 다양한 문제가 있으니 다른 사람의 풀이를 참고하면 새로운 코드를 알 수 있다. 

def solution(dart_result):
    sdt = ' SDT'
    ans = []
    idx = 0
    for i , c in enumerate(dart_result):
        if c in sdt:
            ans.append(int(dart_result[idx:i]) ** sdt.index(c))
        elif c == '#':
            ans[-1] = -ans[-1]
        elif c == '*':
            ans[-1] <<= 1
            if len(ans) >= 2:
                ans[-2] <<=1
        
        if not c.isdecimal():
            idx = i+1

    return sum(ans)
