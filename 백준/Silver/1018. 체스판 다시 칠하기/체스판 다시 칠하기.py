import sys

input = sys.stdin.readline
n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]

def check_repainting(start_x, start_y):
    count_w = repainting_w(start_x, start_y)
    count_b = repainting_b(start_x, start_y)
    return min(count_w, count_b)

def repainting_w(start_x, start_y):
    count_w = 0

    for i in range(start_x, start_x+8, 2):
        for j in range(start_y, start_y+8, 2):
            if i == start_x and j == start_y:
                if board[i][j] != "W":
                    count_w += 1   
                continue
            if board[i][j] != "W":
                count_w += 1
                continue
        for j in range(start_y+1, start_y+8, 2):
            if board[i][j] != "B":
                count_w += 1
                continue
    for i in range(start_x+1, start_x+8, 2):
        for j in range(start_y, start_y+8, 2):
            if board[i][j] != "B":
                count_w += 1
                continue
        for j in range(start_y+1, start_y+8, 2):
            if board[i][j] != "W":
                count_w += 1
                continue
    return count_w

def repainting_b(start_x, start_y):
    count_b = 0

    for i in range(start_x, start_x+8, 2):
        for j in range(start_y, start_y+8, 2):

            a = board[i][j]
            b = "B"

            if i == start_x and j == start_y:
                if board[i][j] != "B":
                    count_b += 1   
                continue
            if board[i][j] != "B":
                count_b += 1
                continue
        for j in range(start_y+1, start_y+8, 2):

            a = board[i][j]
            b = "W"

            if board[i][j] != "W":
                count_b += 1
                continue
    for i in range(start_x+1, start_x+8, 2):
        for j in range(start_y, start_y+8, 2):

            a = board[i][j]
            b = "W"

            if board[i][j] != "W":
                count_b += 1
                continue    
        for j in range(start_y+1, start_y+8, 2):

            a = board[i][j]
            b = "B"

            if board[i][j] != "B":
                count_b += 1
                continue
    return count_b

result = sys.maxsize
for i in range(n-7):
    for j in range(m-7):
        check_result = check_repainting(i, j)
        result = min(result, check_result)

print(result)