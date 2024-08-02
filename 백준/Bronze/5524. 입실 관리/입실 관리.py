import sys
input = sys.stdin.readline

n = int(input().strip())

name_list = [input().strip().lower() for _ in range(n)]

print(*name_list, sep="\n")