N, K = map(int, input().split())
time = 0
a = 0
b = 0

while True:
    N*=2
    time+=1
    if N < K:
        a = K - N - 1

    elif N > K:
        b = N - K - 1
        if b < a:
            time += b
            break
        else:
            time-=1
            time+=a
            break

print(time)