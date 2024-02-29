import sys
input = sys.stdin.readline

N = int(input())

list = [list(map(int, input().split())) for _ in range(N)]

rank = [1] * len(list)

for i in range(N):
    for j in range(N):
        if list[i][0] < list[j][0] and list[i][1] < list[j][1]:
            rank[i] += 1

for i in rank:
    print(i)