N = int(input())

list = [i for i in range(1, N+1)]

count = 0

p = 1

for i in list:
    p *= i

p_list = []

for i in str(p):
    p_list.append(i)

p_list.reverse()

for i in p_list:
    if i == "0":
        count += 1
    else:
        break

print(count)