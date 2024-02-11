import sys
input = sys.stdin.readline

N, K = map(int, input().split())

list = [i for i in range(1, N+1)]

queue = []

curr = 0

while list:
    curr += (K-1)
    curr %= len(list)
    queue.append(list.pop(curr))

output = "<" + ", ".join(str(x) for x in queue) + ">"
print(output)
