import sys
input = sys.stdin.readline

N = int(input())
card_list = sorted(map(int, input().split()))  # 정렬된 리스트
M = int(input())
card = list(map(int, input().split()))

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index

result_list = []

for num in card:
    result = count_by_range(card_list, num, num)
    result_list.append(result)

print(*result_list)