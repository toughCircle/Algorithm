def solution(s):
    answer = True
    
    s_list = []
    for i in s:
        if not s_list:
            s_list.append(i)
        elif s_list[-1] == '(' and i == ')':
            s_list.pop()
        else:
            s_list.append(i)
    
    if s_list:
        answer = False

    return answer