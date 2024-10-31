import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
answer = [0] * n
num = 0

def bfs(graph, start, num):
    queue = deque([start]) # 방문 가능 노드
    while queue: # 방문 가능한 노드가 있는 경우
        node = queue.popleft() # 현재 노드

        if not visited[node]:
            num = num + 1
            visited[node] = True # 방문 처리
            queue.extend(sorted(graph[node]))
            answer[node-1] = num
            
bfs(graph, r, num)

for i in answer:
    print(i)