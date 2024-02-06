import sys
input = sys.stdin.readline

K = int(input())

result = []

for i in range(K):
    num = int(input())

    if num == 0:
        result.pop()
    else:
        result.append(num)



print(sum(result))