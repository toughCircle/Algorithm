import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
K = int(input())

index = len(arr) // K
sort_arr = []

for i in range(0, N, index):
    sort_arr = arr[i:i+index]
    sort_arr.sort()
    for j in sort_arr:
        print(j, end = ' ')
