# enter인 사람은 집합에 넣는다. leave인 사람은 집합에서 제거한다.
import sys

input = sys.stdin.readline
s = set()
for _ in range(int(input())):
    name, el = input().split()
    if el == 'enter':
        s.add(name)
    else :
        if name in s:
            s.remove(name)
# 내림차순 정렬 
for name in sorted(s, reverse=True):
    print(name)