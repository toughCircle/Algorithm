import sys
input = sys.stdin.readline

N = int(input())

count = 0

def sugar(N):
    for bags_5 in range(N // 5, -1, -1):
        weight = N - (bags_5 *5)
        if weight % 3 == 0:
            bags_3 = weight // 3
            return bags_5 + bags_3
        
    return -1
    

print(sugar(N))