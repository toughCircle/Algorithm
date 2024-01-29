N = int(input().rstrip())

list = []

for _ in range(N):
    string = input().rstrip()
    if string not in list:
        list.append(string)

list.sort(key=lambda x: (len(x), x))

for i in list:
    print(i)