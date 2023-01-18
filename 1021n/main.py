N, M = map(int, input().split())
loc = list(map(int, input().split()))
q = []
cnt = 0

for k in range(N):
    q.append(k+1)

for i in range(M):
    l = loc[i]
    while(True):
        if q[0] == l:
            q.pop(0)
            break
        else:
            L = q.index(l)
            if L > (len(q)/2):
                n = q.pop()
                q.insert(0, n)
            elif L <= (len(q)/2):
                n = q.pop(0)
                q.append(n)
            cnt+=1

print(cnt)







