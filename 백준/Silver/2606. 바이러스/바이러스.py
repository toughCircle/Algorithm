import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())

graph = {}

for _ in range(M):
    u, v = input().strip().split()
    
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    
    graph[u].append(v)
    graph[v].append(u)

from collections import deque

def bfs(start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        if node not in visited:
            visited.add(node)
            queue.extend(graph.get(node, []))
    
    return visited

connected_nodes = bfs('1')
print(len(connected_nodes) - 1)