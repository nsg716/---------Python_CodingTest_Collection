# 적어도라는 말은 저작권이 있는 곡의 평균의 최소치에서 마지막 값의 +1 을 하면 그 곡의 평균의 최소이며 적어도 저작권이 몇곡이 있는지 알 수 있다.
a, b = map(int, input().split())
print(a*(b-1)+1) # a : 앨범에 수록된 곡, b 는 평균 /