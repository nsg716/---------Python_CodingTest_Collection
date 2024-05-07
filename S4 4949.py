# 괄호 문제 
while (1):
    x= []
    ip = input()
    if(ip == "."):
        break
    

    for i in ip:
        if (i == "(" or i == "["):
            x.append(i)
        
        elif(i == ")"):
            if len(x) != 0 and x[-1] == "(":
                x.pop()
            else:
                x.append(')')
                break
        elif(i == "]"):
            if len(x) != 0 and x[-1] == "[":
                x.pop()
            else:
                x.append(']')
                break
                    
    if len(x) == 0:
        print("yes")
    else:
        print("no")
    

    