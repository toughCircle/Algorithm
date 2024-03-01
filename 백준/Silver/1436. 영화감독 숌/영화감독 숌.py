N = int(input())

i = 1

while True:
    i += 1

    if "666" in str(i):
        N -= 1

    if N == 0:
        print(i)
        break