# 헛간 청약
# 수학

N,W,H,L = map(int, input().split() )

w_count = W // L
h_count = H // L

result = w_count * h_count

print(min(result,N))