import sys
import math
input = sys.stdin.readline

x, y = map(int, input().split())

primeNumber = []

for i in range(x, y+1):
    if i < 2:
        continue

    elif i == 2:
        primeNumber.append(i)
        continue

    isPrime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if (i % j == 0):
            isPrime = False
            break

    if isPrime:
        primeNumber.append(i)

for _ in primeNumber:
    print(_)