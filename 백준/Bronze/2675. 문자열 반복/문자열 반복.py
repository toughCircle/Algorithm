import sys

input = sys.stdin.readline

T = int(input());

for i in range(T):
    R, S = map(str, input().split())
    R = int(R)
    


    for j in S :
        for i in range(R) :
            print(j, end="")
        
    print("")