def d(n):
    n = n+ sum(map(int,str(n)))
    return(n)

non = set()

for i in range(1,10001):
    non.add(d(i))

for j in range(1,10001):
    if j not in non:   
       print(j) 