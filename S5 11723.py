import sys 
input = sys.stdin.readline

N = int(input())
S = set()

for i in range(N):
    text = input().rstrip().split()

    if(len(text) == 1):
        if text[0] == "all":
            S = set([i for i in range(1,21)])
        else: 
            S = set()
            
    else:
        keyword, M  = text[0], text[1]
        M = int(M)
        
        if keyword == "add":
            S.add(M)
        elif keyword =="remove":
            S.discard(M)
        elif keyword == "check":
            print(1 if M in S else 0)
        elif keyword == "toggle":
            if M in S:
                S.discard(M)
            else:
                S.add(M)