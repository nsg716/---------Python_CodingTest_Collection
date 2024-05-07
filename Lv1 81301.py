# 문제 8번 : 숫자 문자열과 영단어  
# replace 를 알면 아주 간단히 풀 수 있는 문제

def solution(s):
    numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(10):
        s = s.replace(numbers[i], str(i))
    return int (s)