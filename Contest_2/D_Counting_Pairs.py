"""t = int(input())
for i in range(t):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    tot = sum(a)
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if tot - (a[i] + a[j]) in range(x, y+1):
                count +=1
    print(count)"""
from bisect import bisect_left, bisect_right
t = int(input())
for i in range(t):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    count = 0
    total = sum(a)
    for i in range(len(a)):
        upper = total - a[i]-x
        lower = total - a[i]-y
        upinde = bisect_right(a, upper)
        dninde = bisect_left(a, lower)
        if dninde <= i:
            dninde = i + 1
        if dninde <= upinde:
            count += upinde - dninde
    print(count)


