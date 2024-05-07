x = ["A+", "A0","B+","B0","C+","C0","D+","D0","P","F"]
dev = 0
ttt = 0
count = 0
N = int(input())
for i in range(N) :
    name, num, ave = input().split()
    num = float(num)

    if ave == "A+" :
        dev = 4.3
        ttt += num
        count += (float(num)*dev)
    elif ave == "A0" :
        dev = 4.0
        ttt += num
        count += (float(num)*dev)
    elif ave == "A-" :
        dev = 3.7
        ttt += num
        count += (float(num)*dev)

    elif ave == "B+" :
        dev = 3.3
        ttt += num
        count += (float(num)*dev)
    elif ave == "B0" :
        dev = 3.0
        ttt += num
        count += (float(num)*dev)
    elif ave == "B-" :
        dev = 2.7
        ttt += num
        count += (float(num)*dev)

    elif ave == "C+" :
        dev = 2.3
        ttt += num
        count += (float(num)*dev)
    elif ave == "C0" :
        dev = 2.0
        ttt += num
        count += (float(num)*dev)
    elif ave == "C-" :
        dev = 1.7
        ttt += num
        count += (float(num)*dev)

    elif ave == "D+" :
        dev = 1.3
        ttt += num
        count += (float(num)*dev)
    elif ave == "D0" :
        dev = 1.0
        ttt += num
        count += (float(num)*dev)
    elif ave == "D-" :
        dev = 0.7
        ttt += num
        count += (float(num)*dev)    
    elif ave == "F"  :
        dev = 0.0
        ttt += num
        count += (float(num)*dev)

result = count / ttt
print("%.2f" % round(result + 10**-10, 2))