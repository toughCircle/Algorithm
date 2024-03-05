import sys
input = sys.stdin.readline

N, M = map(int, input().split())

coin = [int(input()) for _ in range(N)]

coin.reverse()

count = 0

for i in coin:
    if i <= M:
        count += M // i
        M = M % i
    if M == 0:
        break

print(count)