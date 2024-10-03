def solution(fees, records):
    from collections import deque
    import math
    
    answer = []
    
    # 차량번호 별 주차 시간 기록을 위한 맵
    parking_records = {}
    
    for i in records:
        time, num, log = i.split()

        if num not in parking_records:
            parking_records[num] = deque()
            
        # 분 단위로 변환 후 저장
        minute = int(time[:2]) * 60 + int(time[3:])
        parking_records[num].append([minute, log])

    parking_records = dict(sorted(parking_records.items()))

    # 각 주차 시간 계산
    for i in parking_records:
        parking_times = []
        
        while parking_records[i]:
            log = parking_records[i].popleft()
            
            if log[1] == "IN":
                enter_time = log[0]
                
                # 출차 기록이 없는 경우
                if len(parking_records[i]) == 0:
                    exit_time = 1439
                    parking_times.append(exit_time - enter_time)

            if log[1] == "OUT":
                exit_time = log[0]
                parking_times.append(exit_time - enter_time)
        
        # 총 주차 시간 계산
        total_time = sum(parking_times)
        
        # 기본 시간 초과 여부에 따른 요금 계산
        if total_time <= fees[0]:
            fee = fees[1]  # 기본 요금
        else:
            extra_time = total_time - fees[0]
            extra_fee = math.ceil(extra_time / fees[2]) * fees[3]
            fee = fees[1] + extra_fee

        # 요금을 정수로 변환해서 answer에 추가
        answer.append(int(fee))

    return answer