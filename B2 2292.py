N = int(input())
N_count= 1 #초기위치
count= 1 #초기 방 개수 

while N > N_count :
    N_count += 6*count # 방개수 영역 확장 
    count+=1

print(count)