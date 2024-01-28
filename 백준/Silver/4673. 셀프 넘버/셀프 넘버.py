result = []

for i in range(1, 10001):

    digits = [int(digit) for digit in str(i)]
    new_i = i

    for j in digits:
        new_i += j
    result.append(new_i)
    
    result_set = set(result)
    
    if i not in result_set:
        print(i)