#문자열 2개 입력, 그 문자열의 순서를 뒤집고, 크기를 비교한 후 큰 문자열을 출력

a, b = (map(int, input().split()))

al = int(str(a)[::-1]) 
bl = int(str(b)[::-1]) 




if int(al) > int(bl) :
    print(al)
else: 
    print(bl)
