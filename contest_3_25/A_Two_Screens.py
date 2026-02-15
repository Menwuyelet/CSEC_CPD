q = int(input())
for i in range(q):
    s = input()
    t = input()

    count = len(s) + len(t)
    if len(s) > len(t):
        if t == s[0:len(t)]:
            count -= len(t)-1
    elif len(t) > len(s):
        if s == t[0:len(s)]:
            count -= len(s)-1

    print(count)