N = int(input()) # 횟수 정하기 
val = []
stk = []
s = input() # 후위표기식 입력 
for _ in range(N):  # 횟수 반복하여 출력 
    val.append(int(input()))

for ch in s:
    if ch.isalpha():
        stk.append(val[ord(ch) - ord('A')]) # 문자량의 차이 만큼 넣는다. 문자의 순서 위치값에 따른 차이값을 넣는다.
    
    else: # 알파벳이 아니면 연산자가 들어왔다는 의미이다. 
        b = stk.pop() # 순서 주의 
        a = stk.pop()
        if ch == '+':
            stk.append(a+b)
        elif ch == '-':
            stk.append(a-b)
        elif ch == '*':
            stk.append(a*b)
        elif ch == '/':
            stk.append(a/b)
print(f'{stk[0]:.2f}') # f-stirng 방식 ,소수점 둘째자리까지 표시