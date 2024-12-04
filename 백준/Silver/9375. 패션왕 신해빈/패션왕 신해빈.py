import sys
from math import prod

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    if N == 0:
        print(N)
        continue
    
    wear = dict()
    for _ in range(N):
        i, j = input().split()
        if j not in wear:
            wear[j] = 1
        else:
            wear[j] += 1
    
    print(prod(count + 1 for count in wear.values()) - 1)
