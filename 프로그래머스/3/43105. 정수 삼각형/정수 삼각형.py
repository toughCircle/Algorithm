def solution(triangle):
    answer = 0

    dp = [row[:] for row in triangle]
    n = len(triangle)

    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            dp[i][j] += max(dp[i + 1][j], dp[i + 1][j + 1])

    answer = dp[0][0]

    return answer