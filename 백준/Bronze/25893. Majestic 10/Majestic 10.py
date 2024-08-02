import sys
input = sys.stdin.readline

n = int(input().strip())
num_list = [input().split() for _ in range(n)]

for i in num_list:
    count = 0
    for j in i:
        if int(j) < 10:
            continue
        if int(j) % 10 == 0:
            count += 1
    if count == 0:
        print(*i, '\nzilch\n')
    if count == 1:
        print(*i, '\ndouble\n')
    if count == 2:
        print(*i, '\ndouble-double\n')
    if count == 3:
        print(*i, '\ntriple-double\n')