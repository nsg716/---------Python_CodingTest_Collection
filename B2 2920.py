a = list(map(int, input().split()))
count1 = 0
count2 = 0
count = 0
for i in range(1,len(a)+1):
    if a[i-1] == i:
        count1 += 1
    elif a[i-1] == 9-i:
        count2 += 1


if count1 == 8:
    print("ascending")
elif count2 == 8:
    print("descending")
else :
    print("mixed")