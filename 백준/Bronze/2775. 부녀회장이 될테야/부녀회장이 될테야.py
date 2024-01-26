T = int(input())

for i in range(T) :
    apartment = []
    ans = 0

    K = int(input())
    N = int(input())

    for i in range(K+1):
        new_f = []
        h = 0;
        for j in range(N):
            if i == 0:
                new_f.append(j+1)
                # apartment.append(new_f)
            else: 
                h += apartment[i-1][j]
                new_f.append(h)
        apartment.append(new_f)

    print(apartment[K][N-1])