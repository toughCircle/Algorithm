import sys
input = sys.stdin.readline

N = input()

if int(N) < 10:
    new_N = "0"+N
else:
    new_N = N

count = 0

while True:
    n1 = new_N[1]
    plusN = int(new_N[0]) + int(new_N[1])
    n2 = str(plusN)[-1]
    n3 = n1 + n2
    count+=1

    if int(n3) == int(N):
        break
        
    else:
        new_N = n3

print(count)

