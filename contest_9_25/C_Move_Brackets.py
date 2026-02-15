t = int(input())
for _ in range(t):
    n = int(input())
    stack = list(input())
    count = 0
    new_stack = {'(':0}
    for chr in stack:
        if chr == "(":
            new_stack['('] += 1
        else:
            if new_stack['('] > 0:
                new_stack['('] -= 1
            else:
                count += 1
    print(count)