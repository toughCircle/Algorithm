import sys
input = sys.stdin.readline

N = int(input())

score = [int(input()) for _ in range(N)]

dp = [0] * 300

dp[0] = score[0]
if N > 1:
    dp[1] = max(score[0] + score[1], score[1])
if N > 2:
    # 마지막 계단을 항상 밟아야 함
    dp[2] = max(score[0] + score[2], score[1] + score[2])

for i in range(3, N):
    # 이전 계단을 밟지 않는 경우와 이전 계단을 밟는 경우로 두 가지 경우
    # 3 -> 0, 1, 3 / 0, 2, 3
    dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])

print(dp[N-1])