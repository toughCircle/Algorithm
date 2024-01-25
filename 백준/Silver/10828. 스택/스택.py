import sys
input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n) :
    command = input().rstrip()
    if command[:4] == "push" :
        i = int(command[5:])
        arr.append(i)
    if command == "top" :
        if len(arr) > 0 :
            print(arr[-1])
        else :
            print(-1)
    if command == 'size' :
        print(len(arr))
    if command == "pop" :
        if len(arr) > 0 : 
            print(arr.pop())
        else :
            print(-1)
    if command == "empty" :
        if len(arr) == 0 :
            print(1)
        else :
            print(0)