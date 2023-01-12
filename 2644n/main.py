n = int(input())
a, b = map(int, input().split())
m = int(input())
chon = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
res = []

for _ in range(m):
    x, y = map(int, input().split())
    chon[x].append(y)
    chon[y].append(x)

def dfs(s, num):
    num += 1
    visited[s] = 1

    if s == b:
        res.append(num)

    for i in chon[s]:
        if visited[i] == 0:
            dfs(i, num)

dfs(a, 0)
if len(res) == 0:
    print(-1)
else:
    print(res[0]-1)