def solution(today, terms, privacies):
    answer = []
    
    d = list(map(int, today.split('.')))
    
    t = {}
    
    for i in terms:
        j = i.split()
        t[j[0]] = int(j[1])
        
    p = [i.split() for i in privacies]
    
    for i in range(len(p)):
        p_d = list(map(int, p[i][0].split('.')))
        # 수집일 + 유효기간 (m)
        p_d[1] += t[p[i][1]]
        # 12월을 넘기는 경우
        if p_d[1] > 12:
            p_d[0] += p_d[1] // 12
            if p_d[1] % 12 == 0:
                p_d[0] -= 1
                p_d[1] = 12
            else:
                p_d[1] = p_d[1] % 12
        
        # 오늘 날짜와 비교
        if p_d[0] < d[0]:
            answer.append(i+1)
        elif p_d[0] == d[0]:
            if p_d[1] < d[1]:
                answer.append(i+1)
            elif p_d[1] == d[1]:
                if p_d[2] <= d[2]:
                    answer.append(i+1)
    
    return answer