def solution(n):

    from collections import deque

    # 삼각형 배열 생성
    triangle = [[0] * (i + 1) for i in range(n)]
    
    # 방향 아래 -> 오른쪽 -> 위
    directions = deque([(1,0), (0,1), (-1,-1)])

    # 시작 지점
    x, y = 0, 0

    # 숫자 채우기
    for num in range(1, n * (n + 1) // 2 + 1):
        triangle[x][y] = num
        
        new_x = x + directions[0][0]
        new_y = y + directions[0][1]

        # 삼각형의 범위를 넘기거나 값이 이미 채워진 경우 방향 전환
        if not (0 <= new_x < n and 0 <= new_y <= new_x) or triangle[new_x][new_y] != 0:
            # 큐 가장 앞에 있는 값을 맨 뒤로 보냄
            directions.rotate(-1)
            new_x = x + directions[0][0]
            new_y = y + directions[0][1]
        
        # 위치 이동
        x, y = new_x, new_y
    
    answer = []
    for row in triangle:
        answer.extend(row)

    return answer