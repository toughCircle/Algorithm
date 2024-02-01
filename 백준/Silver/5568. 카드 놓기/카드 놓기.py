from itertools import permutations

n = int(input())
k = int(input())

numbers = []

for i in range(n):
    numbers.append(input())

def unique_permutations(elements, length):
    seen = set()
    for p in permutations(elements, length):
        serialized = ''.join(p)
        seen.add(serialized)
    return len(seen)

print(unique_permutations(numbers, k))