N, C =map(int, input().split())
items = []
for i in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

dp = []
tmp = [0]*(C+1)
dp.append(tmp)
for i in range(N):
    w, v = items[i]
    temp = []
    for c in range(C+1):
        if c >= w:
            temp.append(max(dp[i][c-w] + v, dp[i][c]))
        else:
            temp.append(dp[i][c])
    dp.append(temp)

print(dp[N][C])