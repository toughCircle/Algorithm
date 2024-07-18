import sys
input = sys.stdin.readline

S = []

M = int(input().strip())
for _ in range(M):
    req = input().split()
    
    if len(req) == 2:
        if req[0] == "add":
            if S.count(req[1]) != 0:
                continue
            else:
                S.append(req[1])
        if req[0] == "remove":
            if S.count(req[1]) == 0:
                continue
            else:
                S.remove(req[1])
        if req[0] == "check":
            if S.count(req[1]) != 0:
                print(1)
            else:
                print(0)
        if req[0] == "toggle":
            if S.count(req[1]) != 0:
                S.remove(req[1])
            else:
                S.append(req[1])
    if req[0] == "all":
        S.clear()
        S = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    if req[0] == "empty":
        S.clear()