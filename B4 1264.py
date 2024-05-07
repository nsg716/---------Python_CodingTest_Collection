while 1:
    a = input()
    a = a.lower() 
    r = a.count('a') + a.count('e') +a.count('i') + a.count('o') +a.count('u')  
    
    if (a == '#'):
        break
    print(r)