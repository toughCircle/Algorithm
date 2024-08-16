def solution(bridge_length, weight, truck_weights):
    from collections import deque
    answer = 0
    t = deque(truck_weights)
    b = deque([0] * bridge_length)

    while True:
        # 대기중인 차가 없는 경우
        if not t:
            # 다리 위 차가 존재하면
            if sum(b) != 0:
                # 모든 차가 출차할 동안 차량 이동, 1초 증가
                while sum(b) != 0:
                    b.popleft()
                    answer += 1
            break

        # 현재 대기 차량
        i = t.popleft()

        # 다리 위 차 무게 합 + 현재 대기 차 무게 <= 최대 무게
        if sum(b) + i <= weight:
            if len(b) == bridge_length - 1:
                b.append(i)
                answer += 1
                continue
            else:
                b.popleft()
                b.append(i)
                answer += 1
                continue

        # 다리 위 차 무게 합 + 현재 대기 차 무게 > 최대 무게
        if sum(b) + i > weight:
            if len(b) == bridge_length - 1:
                b.append(0)
                answer += 1
                t.appendleft(i)
                continue
            # 만약 가장 앞 차가 없다면 이동만, 1초 증가
            if b[0] == 0 :
                while b[0] == 0:
                    b.append(b.popleft())
                    answer += 1
            # 가장 앞 차가 존재하면 출차, 1초 증가
            b.popleft()
            t.appendleft(i)
            continue 
    return answer