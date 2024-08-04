def solution(array, commands):
    answer = []
    for i, j, k in commands:
        sliced_list = sorted(array[i-1:j])
        answer.append(sliced_list[k-1])
    return answer