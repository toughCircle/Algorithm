def solution(participant, completion):
    answer = []
    from collections import Counter
    count_p = Counter(participant)
    count_c = Counter(completion)

    for item in count_p:
        if count_p[item] > count_c[item]:
            answer.extend([item] * (count_p[item] - count_c[item]))

    return "".join(answer)