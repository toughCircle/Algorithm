def solution(priorities, location):
    from collections import deque
    answer = []
    queue = deque([[i, priorities[i]] for i in range(len(priorities))])

    while queue:
        i = queue.popleft()
        if any(i[1] < j[1] for j in queue):
            queue.append(i)
        
        else:
            answer.append(i[0])
            if i[0] == location:
                return answer.index(i[0]) + 1