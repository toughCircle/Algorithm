import sys
input = sys.stdin.readline

N = int(input().strip())

time = [tuple(map(int, input().split())) for _ in range(N)]

# 종료 시간을 기준으로 정렬 (종료 시간이 같으면 시작 시간을 기준으로 정렬)
time.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for start, end in time:
    if start >= end_time:
        count += 1
        end_time = end

print(count)