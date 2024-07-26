import sys
input = sys.stdin.readline

N, M = map(int, input().split())

result = []
names = set()

for _ in range(N + M):
    name = input().strip()
    if name in names:
            result.append(name)
    else:
        names.add(name)
            
result.sort()
print(len(result))
print(*result, sep='\n')