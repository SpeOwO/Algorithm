n = int(input())
tp = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 6)

for idx, e in enumerate(tp[::-1]):
    if idx == 0 and e[0] == 1:
        dp[n - 1] = e[1]
    elif idx + 1 < e[0]:
        dp[n - idx - 1] = dp[n - idx]
        continue
    else:
        dp[n - idx - 1] = max(dp[n - idx], dp[n - idx - 1 + e[0]] + e[1])

print(dp[0])