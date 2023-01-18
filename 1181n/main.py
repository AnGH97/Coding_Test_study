N  = int(input())
D = []
for _ in range(N):
    d = input()
    D.append(d)

DIC = list(set(D))
dic = []

for i in DIC:
    dic.append((len(i), i))

res = sorted(dic)

for l, w in res:
    print(w)
