import sys
input = sys.stdin.readline

line = []

while True:
    temp = input()
    if temp.rstrip() == ".":
        break
    else:
        line.append(temp.rstrip())

# print(line)


for i in line:
    stack = []
    is_balanced = True
    for char in i:
        if char == "(" or char == "[":
            stack.append(char)
        
        if char == ")":            
            if not stack or stack[-1] != "(":
                is_balanced = False

            elif stack:
                stack.pop()

        if char == "]":            
            if not stack or stack[-1] != "[":
                is_balanced = False
            
            elif stack:
                stack.pop()
            
    if stack or not is_balanced:
        print("no")

    else:
        print("yes")