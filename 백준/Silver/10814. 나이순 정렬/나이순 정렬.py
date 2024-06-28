import sys
input = sys.stdin.readline

N = int(input())

user_list = []

for _ in range(N):
    user = list(map(str, input().split()))
    age = int(user[0])
    name = user[1]
    user_list.append([age, name])

user_list.sort(key=lambda x: x[0])

for i in user_list:
    print(i[0], i[1])