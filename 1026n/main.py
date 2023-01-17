N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sum = 0
A.sort()

for i in range(N):
    b = max(B)
    loc = B.index(b)
    B.pop(loc)
    s = A[i] * b
    sum+=s
print(sum)



