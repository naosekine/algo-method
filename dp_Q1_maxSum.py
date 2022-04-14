n = int(input())
A = list(map(int, input().split()))

dp = [0]
for i in range(n):
    dp.append(max(dp[i] + A[i], dp[i]))
print(dp[-1])