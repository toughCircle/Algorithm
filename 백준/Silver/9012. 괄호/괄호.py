import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    PS = input().rstrip()
    checkList = []

    for i in range(len(PS)):
        if PS[i] == "(":
            checkList.append(PS[i])
        if PS[i] == ")":
            if len(checkList) > 0 and checkList[-1] == "(":
                checkList.pop()
            else:
                checkList.append(PS[i])
    
    if len(checkList) == 0:
        print("YES")
    else:
        print("NO")