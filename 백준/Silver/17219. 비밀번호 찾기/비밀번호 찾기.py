import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memo = dict()

for _ in range(n):
    i, j = input().split()

    memo[i] = j

for _ in range(m):
    i = input().rstrip()
    print(memo[i])