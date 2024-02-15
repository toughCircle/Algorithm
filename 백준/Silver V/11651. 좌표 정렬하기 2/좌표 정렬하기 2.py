import sys
input = sys.stdin.readline

N = int(input())
coordinate = []

for _ in range(N):
    coordinate.append(tuple(list(map(int, input().split()))))

coordinate.sort(key = lambda x : (x[1], x[0]))

for i, j in coordinate:
    print(i, j)