t = int(input())
for _ in range(t):
    s = input()
    state = s[0]
    start = False
    zero = 0
    one = 0
    for _ in s[1:]:
        if _ != state:
            start = True
            # if state == "1":
            #     zero += 1
            # else:
            #     one += 1
        if start:
            if _ == "0":
                zero += 1
            else:
                one += 1
    print(min(zero, one))