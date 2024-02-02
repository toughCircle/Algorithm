import sys
input = sys.stdin.readline

N = int(input())

nums = [0]*10000

for i in range(N):
    num = int(input())
    nums[num-1] += 1

for i in range(10000):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i+1)