def count_ways(n, m):
    dp = [[0 for _ in range(m+2)] for _ in range(n+2)]
    dp[2][2] = 1

    for i in range(2, n+2):
        for j in range(2, m+2):
            dp[i][j] += dp[i-2][j-1] + dp[i-1][j-2]

    return dp[n+1][m+1]

n, m = map(int, input().split())
print(count_ways(n, m))