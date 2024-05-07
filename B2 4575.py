
while True:
    a = input()
     
    b = a.replace(" ", "")
    if a == "END":
        break
    
    sum = 0
    for i in a:
        if i == " ":
            continue
        else :
            sum += a.count(i)
    
    if sum == len(b):
        print(a)
    