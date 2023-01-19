N = int(input())
num = int(input())
snail = [[0] * N for _ in range(N)]
mid = (N-1)//2
u = mid - 1
d = mid + 1
loc1 = loc2 = mid

n = 1
snail[mid][mid] = n

while(True):
    #위
    for i in range(loc1 - 1, u - 1, -1):
        n+=1
        snail[i][loc2] = n
    loc1 = u

    #오른쪽
    for j in range(loc2 + 1, d + 1, 1):
        n+=1
        snail[loc1][j] = n
    loc2 = d

    #아래
    for k in range(loc1 + 1, d + 1, 1):
        n+=1
        snail[k][loc2] = n
    loc1 = d

    #왼쪽
    for l in range(loc2 - 1, u - 1, -1):
        n+=1
        snail[loc1][l] = n
    loc2 = u

    #위
    for m in range(loc1 - 1, u - 1, -1):
        n+=1
        snail[m][loc2] = n
    loc1 = u
    u-=1
    d+=1
    if loc1 == 0 and loc2 == 0:
        break

print(snail)

for i in range(N):
    for j in range(N):
        if snail[i][j] == num:
            print(i+1, j+1)
            break
