import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    I = list(map(int, input().split()))
    target = M
    result = 0

    while True:
        if I[0] == max(I):
            result += 1
            if target == 0:
                print(result)
                break
            else:
                I.pop(0)
                target -= 1
        else:
            I.append(I.pop(0))
            target = (target - 1) % len(I)
