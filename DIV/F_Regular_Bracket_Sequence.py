s = input()
stack = []

for chr in s:
    if chr == "(":
        stack.append("(")
    else:
        if stack and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(")")

print(len(s)- len(stack))