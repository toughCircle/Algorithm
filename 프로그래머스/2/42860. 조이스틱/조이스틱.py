def solution(name):
    answer = 0
    n = len(name)

    # 알파벳 변환 
    def get_char_change_cost(char):
        return min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    
    # 알파벳 변환 합산
    for char in name:
        answer += get_char_change_cost(char)
    
    # 커서 이동
    min_move = n - 1  # 오른쪽으로 쭉 가는 경우
    
    for i in range(n):
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
            
        # i 위치에서 커서를 왼쪽으로 돌아가는 경우와 오른쪽으로 계속 가는 경우를 비교
        distance = min(i, n - next_idx)
        min_move = min(min_move, i + n - next_idx + distance)
    
    answer += min_move
    return answer