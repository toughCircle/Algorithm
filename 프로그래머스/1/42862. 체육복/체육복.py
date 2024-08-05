def solution(n, lost, reserve):
    answer = 0
    student_list = [1] * n
    
    for i in lost:
        student_list[i - 1] -= 1
    
    for i in reserve:
        student_list[i - 1] += 1
    
    for i in range(n):
        if student_list[i] == 0:
            if i > 0 and student_list[i - 1] == 2:  
                student_list[i] += 1
                student_list[i - 1] -= 1
            elif i < n - 1 and student_list[i + 1] == 2:
                student_list[i] += 1
                student_list[i + 1] -= 1
                
    for x in student_list:
        if x > 0:            
            answer += 1 
    
    return answer