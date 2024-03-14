import sys
input = sys.stdin.readline

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]
    
def count_color(arr, x, y, N):
    color = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if paper[i][j] != color:
                half = N // 2
                top_left = count_color(paper, x, y, half)
                top_right = count_color(paper, x, y + half, half)
                bottom_left = count_color(paper, x + half, y, half)
                bottom_right = count_color(paper, x + half, y + half, half)
                
                white = top_left[0] + top_right[0] + bottom_left[0] + bottom_right[0]
                blue = top_left[1] + top_right[1] + bottom_left[1] + bottom_right[1]
                return white, blue
    
    return (1, 0) if color == 0 else (0, 1)
    
white, blue = count_color(paper, 0, 0, N)
print(white)
print(blue)