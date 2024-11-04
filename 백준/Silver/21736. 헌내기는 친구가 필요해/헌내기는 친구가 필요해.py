from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
campus = []
start_x, start_y = -1, -1 

for i in range(n):
    k = input().rstrip()
    p = []
    for j in range(m):
        p.append(k[j])
        if k[j] == 'I': # 시작 위치 확인
            start_x, start_y = i, j
    campus.append(p)

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y):
    queue = deque([(x, y)])
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    find = 0

    while queue:
        cx, cy = queue.popleft()

        # 현재 위치가 'P'인 경우
        if campus[cx][cy] == 'P':
            find += 1

        for dx, dy in move:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and campus[nx][ny] != 'X':
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    return find

if start_x != -1:
    answer = bfs(start_x, start_y)
    if answer == 0:
        print("TT")
    else:
        print(answer)
else:
    print("TT")
