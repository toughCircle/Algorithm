import sys
input = sys.stdin.readline

K, N = map(int, input().split())

line_list = [int(input()) for _ in range(K)]

def count_div(list, length):
    count = 0
    for lan in list:
        count += lan // length
    return count

def max_len(list, N):
    left, right = 1, max(list)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if count_div(list, mid) >= N:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result   

max_length = max_len(line_list, N)
print(max_length)