import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
    
    graph[i].sort()
    graph[j].sort()

from collections import deque

visited = []

def dfs(cur_v):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            dfs(v)
    return visited

def bfs(start_v):
    visited = [start_v]
    queue = deque([start_v])
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited

print(*dfs(V))
print(*bfs(V))