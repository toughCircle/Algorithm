import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())

# 관계를 저장할 맵
graph = defaultdict(list)

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

# 베이컨 수 구하기
def bfs(start):
    visit = [-1] * (N + 1) # 방문 노드 리스트
    visit[start] = 0 # 시작 노드 방문 값 수정
    queue = deque([start]) # 시작 노드를 큐에 넣기
    total_distance = 0 # 베이컨 수

    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if visit[n] == -1: # 방문한 적 없는 노드일 경우
                visit[n] = visit[node] + 1
                total_distance += visit[n]
                queue.append(n)
    return total_distance


bacon = []
for i in range(1, N + 1):
    bacon.append((bfs(i), i))

bacon.sort()
print(bacon[0][1])