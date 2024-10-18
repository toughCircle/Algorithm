def solution(n, wires):
    from collections import defaultdict
    
    # 인접리스트 저장
    graph = defaultdict(list)
    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)
    
    # 트리의 크기 계산
    def dfs(node, visited):
        visited.add(node)
        count = 1  # 서브 트리의 크기
        for neighbor in graph[node]:
            if neighbor not in visited:
                count += dfs(neighbor, visited)
        return count
    
    min_difference = n  # 차이의 최솟값을 구하기 위해 초기화
    
    # 전선을 하나씩 끊어 계산
    for u, v in wires:
        graph[u].remove(v)
        graph[v].remove(u)
        
        visited = set()
        subtree_size = dfs(u, visited)  # u에서 시작하는 서브 트리의 크기 계산
        difference = abs((n - subtree_size) - subtree_size)
        min_difference = min(min_difference, difference)
        
        # 전선을 원복
        graph[u].append(v)
        graph[v].append(u)
    
    return min_difference
