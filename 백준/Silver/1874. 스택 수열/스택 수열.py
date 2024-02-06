import sys
input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]

stack = []
result = []
curr = 1

for target in numbers:

    while curr <= target:
        stack.append(curr)
        result.append("+")
        curr += 1

    if stack[-1] == target:
        stack.pop()
        result.append("-")

    else:
        print("NO")
        break

else:
    for i in result:
        print(i)
    