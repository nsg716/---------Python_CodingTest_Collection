str = input().upper() # 문자를 입력 -> 대문자
new_str = list(set(str)) # 입력 받은 문자를 중복 없이 하여 새로운 리스트 생성

x = [] # 리스트 빈것
for i in new_str :
    count = str.count(i) # 문자 숫자만큼 카운트 , 순서는 무작위 
    x.append(count)# 순서가 무작위인 숫자를 리스트에 추가 

if x.count(max(x)) > 1: # 최댓값이 2개 이상이면
    print("?")
else :  # 그게 아니면
    max = x.index(max(x)) #무작위인 리스트 최댒값의 주소를 max 변수에 저장
    print(new_str[max]) # 주소에 담긴 리스트 요소 출력

