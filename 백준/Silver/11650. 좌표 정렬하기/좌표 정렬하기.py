import sys
input = sys.stdin.readline

N = int(input())

list = [tuple(map(int,input().split())) for _ in range(N)]

list.sort(key=lambda x: (x[0], x[1]))

for i, j in list:
    print(i, j)
