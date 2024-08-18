def solution(sizes):
    answer = 0
    w = 0
    h = 0
    for i in sizes:
        i.sort()
        w = max(i[0], w)
        h = max(i[1], h)
    answer = w * h
    return answer