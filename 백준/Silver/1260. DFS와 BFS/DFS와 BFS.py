import sys
from collections import defaultdict, deque
input = sys.stdin.readline

# 정점 개수, 간선 개수, 탐색 시작 노드
n, m, v = map(int, input().split())

# 그래프 입력을 위한 맵
graph = defaultdict(list)

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

    # 그래프 정렬
    graph[i].sort()
    graph[j].sort()

def dfs(start): # 깊이
    visited = [] # 방문한 노드
    stack = [start] # 방문가능 노드

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node) # 현재 노드 방문 처리

            for i in range(len(graph[node]) - 1, -1, -1):
                stack.append(graph[node][i]) # 연결된 노드 리스트 추가
    return visited

def bfs(start): # 너비
    visited = [] # 방문한 노드
    queue = deque([start]) # 방문 가능 노드
    visited.append(start)

    while queue:
        node = queue.popleft()

        # 현재 노드의 연결된 모든 노드 방문
        for i in sorted(graph[node]):
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return visited

print(*dfs(v))
print(*bfs(v))
