N = list(input())
for i in range(len(N)):
    if N[i].isupper() == True:
        print(N[i].lower(), end= '')
    else:
        print(N[i].upper(), end= '')