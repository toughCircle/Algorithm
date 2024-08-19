def solution(brown, yellow):
    answer = []
    n = brown + yellow
    j = 0
    for i in range(3, n + 1):
        if n % i == 0:
            j = n // i
            if (i - 2) * (j - 2) == yellow:
                answer.append(i)
                answer.append(j)
                break
    answer.sort(reverse = True)
    return answer