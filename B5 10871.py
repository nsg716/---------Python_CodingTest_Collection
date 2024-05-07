a, b = map(int, input().split()) # 입력받는 수 구별
n_list = list(map(int, input().split())) # 그 이후 입력받는수 배열로 만들기
for i in range(len(n_list)): # 리스트의 크기만큼 실행
   if b > n_list[i] :   # 리스트의 요소가 입력값보다 작으면 
        print(n_list[i], end = ' ') # 해당 리스트 요소 출력