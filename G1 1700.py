# 최적 교체 알고리즘 
N,K = map(int,input().split())
schedule = list(map(int,input().split()))
ans = 0
multi_tap = []
for i,v in enumerate(schedule):
    if v in multi_tap:
        continue
    elif len(multi_tap) < N:
        multi_tap.append(v)
    else:
        ans+=1
        is_found = False
        nxt = (-1,0)
        for j ,val in enumerate(multi_tap):
            if val in schedule[i+1:]: 
                nxt_idx = schedule[i+1:].index(val)
                if nxt[0] <nxt_idx:
                    nxt = (nxt_idx,j)
            else:
                is_found = True
                multi_tap[j] = v
                break

        if not is_found:
            multi_tap[nxt[1]] = v

print(ans)
