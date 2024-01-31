n = int(input())
k = int(input())

numbers = []

for i in range(n):
    numbers.append(input())

def create_permutations(arr, k):
    if k == 0:
        return [[]]

    permutations = []
    for i in range(len(arr)):
        m = arr[i]
        new_arr = arr[:i] + arr[i+1:]

        for p in create_permutations(new_arr, k-1):
            permutations.append([m] + p)

    return permutations

def count_number(numbers, k):
    new_numbers = set()
    for com in create_permutations(numbers, k):
        n = ''.join(com)
        new_numbers.add(n)
    return len(new_numbers)


result = count_number(numbers, k)
print(result)