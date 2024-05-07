books = dict()
for _ in range(int(input())):
    name = input()
    if name in books:
        books[name] += 1
    else:
        books[name] = 1
# books라는 딕셔너리를 만든 이후 그 안에 name이라는 key 가 있으면 value에 +1 없으면 key를 추가하고 value를 1로 설정

max_val = max(books.values()) #딕셔너리중 가장 큰값을 max_val 로 설정 
arr = []
for k, v in books.items(): # 딕셔너리를 반복문으로 돌린다.
    if v == max_val: # 값이 최댓값이면 배열에 저장 
        arr.append(k)

arr.sort() # 같은 값이 있으면 사전순으로 정렬 
print(arr[0]) # 사전순 첫번째 name 입력 