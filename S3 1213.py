# 홀수번째 등장하는 문자는 문자열의 맨 마지막에 배치한 후 문자열을 뒤집는다.
from collections import Counter # 문자가 몇개 등장하였는지에 개수를 딕셔너리 형태로 반환 
alphabet_cnt =Counter(input())

if sum (cnt % 2 for cnt in alphabet_cnt.values()) > 1: # 홀수개인 문자가 1개 초과일경우 
    print("I'm Sorry Hansoo")

else:
    half = ''
    for ch,cnt in sorted(alphabet_cnt.items()):
        half += ch * (cnt//2)
    ans = half
    for ch,cnt in alphabet_cnt.items():
        if cnt %2:
            ans += ch
            break

    ans += ''.join(reversed(half))
    print(ans)