def solution(progresses, speeds):
    answer = []
    day = []
    for i in range(len(progresses)):
        d = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] > 0:
            d += 1
        day.append(d)

    current_day = day[0]
    count = 0

    for d in day:
        if d <= current_day:
            count += 1
        else:
            answer.append(count)
            count = 1
            current_day = d

    answer.append(count)

    return answer