def solution(arr):
    
    def compress(x, y, size):
        initial_value = arr[x][y]
        
        # 해당 영역이 모두 같은 값인지 확인
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != initial_value:
                    # 값이 다르면 4등분하여 재귀 호출
                    new_size = size // 2
                    compress(x, y, new_size)
                    compress(x, y + new_size, new_size)
                    compress(x + new_size, y, new_size)
                    compress(x + new_size, y + new_size, new_size)
                    return
        
        # 모두 같은 값이면 개수 증가
        if initial_value == 0:
            answer[0] += 1
        else:
            answer[1] += 1

    n = len(arr)
    answer = [0, 0]
    compress(0, 0, n)
    
    return answer