import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]

min_height = min(map(min, land))
max_height = min(256, max(map(max, land)) + B)

min_time, best_height = float('inf'), 0

for target_height in range(min_height, max_height + 1):
    add, remove = 0, 0
    for row in land:
        for height in row:
            if height < target_height:
                add += (target_height - height)
            elif height > target_height:
                remove += (height - target_height)
    
    if add <= remove + B:
        time = add + 2 * remove
        if time < min_time or (time == min_time and target_height > best_height):
            min_time = time
            best_height = target_height


print(min_time, best_height)
