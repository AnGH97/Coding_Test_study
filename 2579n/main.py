s = int(input())
stair = [0] * 301
dp = [0] * 301

for i in range(s):
    sc = int(input())
    stair[i] = sc

dp.append(stair[0])
dp[0] = stair[0]
dp[1] = stair[0]+stair[1]
dp[2] = max(stair[0]+stair[2], stair[1]+stair[2])

for i in range(3, s):
    dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])

print(dp[s - 1])









