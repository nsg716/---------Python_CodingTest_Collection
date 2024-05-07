N = int(input())
x = [64]

while True:
    
    if sum(x) > N:
        a = x.pop(-1)
        x.append(a/2)
    elif sum(x) < N:
        a = x[-1]/2
        x.append(a)
    else:
        break
  
print(len(x))