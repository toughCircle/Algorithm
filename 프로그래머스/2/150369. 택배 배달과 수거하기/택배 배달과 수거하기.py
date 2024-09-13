def solution(cap, n, deliveries, pickups):
    answer = 0
    
    # 가장 마지막 집부터 처리하기 위해 스택 사용
    d_stack = []
    p_stack = []

    # 배달과 수거를 스택에 추가 (0인 경우는 추가하지 않음)
    for i in range(n):
        if deliveries[i] > 0:
            d_stack.append((i, deliveries[i]))
        if pickups[i] > 0:
            p_stack.append((i, pickups[i]))
    
    while d_stack or p_stack:
        # 이번에 처리할 최대 거리 (가장 멀리 있는 집)
        max_distance = 0

        # 배달 처리
        current_cap = cap
        while d_stack and current_cap > 0:
            i, amount = d_stack.pop()
            max_distance = max(max_distance, i + 1)
            
            if amount <= current_cap:
                current_cap -= amount
            else:
                d_stack.append((i, amount - current_cap))
                current_cap = 0

        # 수거 처리
        current_cap = cap
        while p_stack and current_cap > 0:
            i, amount = p_stack.pop()
            max_distance = max(max_distance, i + 1)

            if amount <= current_cap:
                current_cap -= amount
            else:
                p_stack.append((i, amount - current_cap))
                current_cap = 0

        # 이번 왕복에 처리한 가장 먼 거리를 두 배로 왕복
        answer += max_distance * 2

    return answer
