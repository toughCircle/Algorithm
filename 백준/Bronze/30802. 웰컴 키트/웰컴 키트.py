import sys
input = sys.stdin.readline

N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())
result = 0

for i in size:
    if (i % T) > 0:
        result += (i // T) + 1
    else:
        result += i//T

print(result)
print(N//P, N%P)