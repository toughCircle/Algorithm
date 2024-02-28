import sys
input = sys.stdin.readline

N = int(input())

def create_array(target):
    curr = 2
    index = 1
    
    if target == 1:
        return 1

    while curr <= target:
        length = 6 * index
        if curr + length > target:
            break
        curr += length
        index += 1

    return index + 1

print(create_array(N))