while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if max(a, b, c) == c:
        if (a * a) + (b * b) == (c * c):
            print('right')
        else:
            print('wrong')
    if max(a, b, c) == b:
        if (a * a) + (c * c) == (b * b):
            print('right')
        else:
            print('wrong')
    if max(a, b, c) == a:
        if (c * c) + (b * b) == (a * a):
            print('right')
        else:
            print('wrong')