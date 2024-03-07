import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())

    land = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(K):
        row, col = map(int, input().split())
        land[row][col] = 1

    def dfs_stack(row, col):
        stack = [(row, col)]  

        while stack:
            x, y = stack.pop()  

            if x < 0 or y < 0 or x >= N or y >= M or land[x][y] == 0:
                continue

            land[x][y] = 0  

            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                stack.append((nx, ny))

    count = 0

    for i in range(N):
        for j in range(M):
            if land[i][j] == 1:
                dfs_stack(i, j)
                count += 1

    print(count)
