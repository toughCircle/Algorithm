import sys
input = sys.stdin.readline

N = int(input())

waiting = sorted(list(map(int, input().split())))

sum_num = 0
sum_list = []

for i in waiting:
    sum_num = sum_num + i
    sum_list.append(sum_num)

print(sum(sum_list))