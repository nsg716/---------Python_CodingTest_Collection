# 문자열 같은지 확인하기 
str = (input())
rev_str = ''
for i in str:
    rev_str = i+ rev_str
if str == rev_str :
    print(1)
else :
    print(0)
