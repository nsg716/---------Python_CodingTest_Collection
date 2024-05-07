int = int(input())
sub = 1
for i in range(1, int + 1): 
    sub += 1
    if ( (int % sub) == 0):
        while (int % sub) == 0 :
            print(sub)
            int = int / sub