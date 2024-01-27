import sys

def plus(n1, n2, N):
    count = 0
    original = n1 + n2

    while True:
        sum_value = int(n1) + int(n2)
        n1 = n2
        n2 = str(sum_value)[-1]
        count += 1

        if n1 + n2 == original:
            break

    return count

N = sys.stdin.readline().strip()

if len(N) == 1:
    N = "0" + N

n1, n2 = N[0], N[1]

print(plus(n1, n2, N))