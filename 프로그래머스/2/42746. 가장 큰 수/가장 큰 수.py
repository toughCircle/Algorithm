from functools import cmp_to_key

def solution(numbers):
    answer = ''
    
    string_list = list(map(str, numbers))
    
    def compare(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0
    
    string_list.sort(key=cmp_to_key(compare))
    
    if string_list[0] == '0':
        return '0'
    
    answer = ''.join(string_list)
    return answer