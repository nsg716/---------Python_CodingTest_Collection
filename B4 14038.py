x = []
for i in  range(6):
    x.append((input()))
if x.count('W') >=5:
    print(1)
elif 5>x.count('W') >=3:
    print(2)
elif 3 >x.count('W') >= 1:
    print(3)
elif x.count('W') == 0:
    print(-1)