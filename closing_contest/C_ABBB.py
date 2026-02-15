t = int(input())
for _ in range(t):
    words = input()
    stack = []
    for ch in words:
        if ch == "B" and stack:
            stack.pop()
        else:
            stack.append(ch)
    print(len(stack))