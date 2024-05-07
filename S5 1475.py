pla = list(input())
lin = ['0','1','2','3','4','5','6','7','8','9']
x = []


for i in lin:
    if i == '6' or i == '9':
        if (pla.count('6')+pla.count('9')) % 2 == 1:
            x.append(int((pla.count('6')+pla.count('9'))/2+1))
        elif (pla.count('6')+pla.count('9')) % 2 == 0:
            x.append(int((pla.count('6')+pla.count('9'))/2))
    else :
        x.append(pla.count(i))

    
print(max(x))