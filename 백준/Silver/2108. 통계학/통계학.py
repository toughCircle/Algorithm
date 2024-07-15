import sys
input = sys.stdin.readline

N = int(input().strip())
num_list = [int(input().strip()) for _ in range(N)]

# 산술 평균
average = sum(num_list) / N
print(round(average))

# 중앙값
sorted_list = sorted(num_list)
print(sorted_list[round(N//2)])

# 최빈값
from collections import Counter

if N < 2:
    print(num_list[0])

else:
    counter = Counter(num_list)
    # 최빈값을 가지는 요소들을 빈도수 순으로 정렬된 리스트로 변환
    sorted_items = counter.most_common()
    # 최빈값의 최대 빈도수를 계산
    max_count = sorted_items[0][1]
    filtered_items = [item for item, count in sorted_items if count == max_count]
    filtered_items.sort()

    # 최빈값 출력
    if len(filtered_items) >= 2:
        print(filtered_items[1])
    else:
        print(filtered_items[0])

# 범위
min_num = min(num_list)
max_num = max(num_list)
print(max_num - min_num)