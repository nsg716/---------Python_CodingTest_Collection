a, b, c = map(int, input().split())
if a+b+c >= 100:
    print("OK")
elif a >= c and b >= c:
    print("Hanyang")
elif c >= a and b >= a:
    print("Soongsil")
elif a >= b and c >= b:
    print("Korea")