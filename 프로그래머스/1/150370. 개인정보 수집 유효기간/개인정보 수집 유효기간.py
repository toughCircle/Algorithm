def solution(today, terms, privacies):
    answer = []
    
    d = list(map(int, today.split('.')))  # 오늘 날짜를 년, 월, 일로 나눔
    
    t = {}
    
    # 약관과 해당 유효기간을 딕셔너리로 저장
    for i in terms:
        j = i.split()
        t[j[0]] = int(j[1])
        
    p = [i.split() for i in privacies]  # 개인정보 수집일과 약관을 분리해서 저장
    
    for i in range(len(p)):
        p_d = list(map(int, p[i][0].split('.')))  # 수집일을 년, 월, 일로 나눔
        # 수집일에 유효기간을 더함
        p_d[1] += t[p[i][1]]  # 유효기간의 n개월을 수집일의 월에 더함
        
        # 월이 12월을 넘기는 경우에 년도를 더해주는 처리
        while p_d[1] > 12:
            p_d[0] += 1
            p_d[1] -= 12
        
        # 만료일은 정확히 계산된 유효기간 끝나는 날의 하루 전이므로 일에서 1을 뺌
        p_d[2] -= 1
        # 만약 일이 0이 된다면, 이전 달의 마지막 날로 처리
        if p_d[2] == 0:
            p_d[1] -= 1
            if p_d[1] == 0:
                p_d[1] = 12
                p_d[0] -= 1
            p_d[2] = 28  # 모든 달을 28일까지 있다고 가정
        
        # 오늘 날짜와 만료일을 비교
        if p_d[0] < d[0] or (p_d[0] == d[0] and p_d[1] < d[1]) or (p_d[0] == d[0] and p_d[1] == d[1] and p_d[2] < d[2]):
            answer.append(i+1)
    
    return answer
