x, y, w, h = map(int, input().split())

a = w - x
b = h - y

if x <= y :
    if a <= x or b <= x :
        if a <= b :
            print(a)
        if b < a :
            print(b)
    else :
        print(x)
elif y <= x :
    if b <= y or a <= y :
        if b <= a :
            print(b)
        if a < b :
            print(a)
    else :
        print(y)
