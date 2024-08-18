def solution(answers):
    from collections import deque
    
    answer_list = [0] * 3
    answers = deque(answers)
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    l = len(answers)
    while answers:
        for i in range(l):
            k = answers.popleft()
            if a[i%len(a)] == k:
                answer_list[0] += 1
            if b[i%len(b)] == k:
                answer_list[1] += 1
            if c[i%len(c)] == k:
                answer_list[2] += 1
            
            
    answer = [i + 1 for i, v in enumerate(answer_list) if v == max(answer_list)]
        
    return answer