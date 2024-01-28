N = int(input().rstrip())
count = N

for i in range(N):
    word = input()
    alphabet = []

    for j in word:
        if j not in alphabet:
            alphabet.append(j)
        else:
            if j == alphabet[-1]:
                pass
            else:
                count -= 1
                break
print(count)