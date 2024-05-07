N = int(input())
aa = ['1','2','3','4','5','6','7','8','9','0']

for i in range(N):
    sum = 0
    s = input()
    for j in range(len(aa)):
        if s.count(aa[j]) > 0:
            sum += 1
    print(sum)
    