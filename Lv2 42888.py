# 문제 2번 : 오픈채팅방
# 마지막에 변경한 닉네임 출력 / 파이썬 딕셔너리의 삽입 삭제는 O(1)이다. 

def solution(record):
    nickname = dict()
    for log in record:
        words = log.split()
        if words[0] in ['Enter','Change']:
            nickname[words[1]] = words[2]
    ans = []
    for log in record:
        words = log.split()
        if words[0] == 'Enter':
            ans.append(f'{nickname[words[1]]}님이 들어왔습니다.')
        elif words[0] =='Leave':
            ans.append(f'{nickname[words[1]]}님이 나갔습니다.')

    return ans 