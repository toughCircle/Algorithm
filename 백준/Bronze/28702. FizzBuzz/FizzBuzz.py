import sys
input = sys.stdin.readline

input_list = [input().strip() for _ in range(3)]

last_num = []

for i in input_list:
    if i.isdigit():
        last_num.append([i, input_list.index(i)])

result_list = last_num[-1]

result = int(result_list[0]) + (3 - result_list[1])
if result % 3 == 0:
    if result % 5 == 0:
        print('FizzBuzz')
    else:
        print('Fizz')

if result % 3 != 0:
    if result % 5 == 0:
        print('Buzz')
    else:
        print(result)