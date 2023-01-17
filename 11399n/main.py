N = int(input())
P = list(map(int, input().split()))
P.sort()
sum = 0
n = 0

for i in range(N):
    n+=P[i]
    sum+=n
print(sum)


