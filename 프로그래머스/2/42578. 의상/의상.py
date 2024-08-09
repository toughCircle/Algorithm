def solution(clothes):

    answer = 1
    clothe_list = {}
    for i, j in clothes:
        if j not in clothe_list:
            clothe_list[j] = []
        if i not in clothe_list[j]:
            clothe_list[j].append(i)

    length = [len(clothe_list[i]) for i in clothe_list]

    for i in length:
        answer *= (i + 1)

    return answer - 1