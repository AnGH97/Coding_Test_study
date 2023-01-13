from collections import deque
m = 100001
res = [0] * m
N, K = map(int, input().split())

def bfs(s, f):
    queue = deque()
    queue.append(s)

    while queue:
        s = queue.popleft()
        if s == f:
            return res[s]
        for ns in (s-1, s+1, 2*s):
            if 0 <= ns < m and not res[ns]:
                res[ns] = res[s] + 1
                queue.append(ns)

print(bfs(N, K))






