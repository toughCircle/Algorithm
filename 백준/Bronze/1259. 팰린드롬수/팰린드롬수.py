while True:
    n = input()

    if n == "0":
        break

    # 순서 뒤집기
    if n == n[::-1]:
        print("yes")

    else:
        print("no")